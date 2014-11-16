# wrimo-grabber 
#  - get and parse tweets for the hashtag
#  - keep only the nice sentences (parsable, not including hashtag) 
#  - save in json file, along with tweet references and pattern's sentiment analysis just for fun
#
# Ranjit Bhatnagar
# for nanogenmo2014
# using pattern from http://www.clips.uantwerpen.be/pattern

from pattern.web import Twitter, SearchEngineLimitError
from pattern.en import parse, parsetree, sentiment

from time import sleep

import io, json

import re 

WORDS_TO_GENERATE = 50000

# if doing multiple searches: put most recent found tweet id here
# so search can stop if it gets there
STOP_AT = "533785825059037184"




twitter = Twitter(language='en')

# collect tweets about #nanowrimo
enough = False
last = None
i = 0
sentences = []
numwords = 0

firsttime = True

while not enough:
	try:
	
		if not firsttime:
			sleep(15)
			firsttime = False
		
		for tweet in twitter.search('#nanowrimo', start=last, count=100):
			i = i + 1
			if tweet.id == STOP_AT:
				print "Reached STOP_AT tweet"
				enough = True
				break
				
			#print i, plaintext(tweet.text)
			last = tweet.id
	
			# skip any tweet with funny characters
			m = re.search(r"[^\w\d\s\'\"\,\.\?\(\)\!\#\@\:]", tweet.text)
			if m:
				#print i, m.group(0), tweet.text
				continue
	
			p = parsetree(tweet.text)
			# keep only sentences that contain a personal pronoun and no unknown parts of speech
			# - the latter should eliminate hashtags (# is tagged as 0/0) and weird garbage
			for sentence in p.sentences:
				# skip sentences containing RT, links, hashtags and @mentions (but keep any other sentences in the tweet)
				if re.search(r'(\bRT\b|http|[\#\@])', sentence.string):
					pass
					#print "HEY!", sentence.string 
				else:
					#print "WHOA", sentence.string, sentence 
					personal = False
					for word in sentence.word:
						if word.type == 'PRP' or word.type == 'PRP$':
							if word.string == "I" or word.string == "me" or word.string == "my":
								personal = True 
					if personal:
						s = ""
						quoting = False
						skipNextSpace = False
						# reassemble sentence from its parts
						for word in sentence.word:
							if len(s) > 0:
								if re.match(r"('ll|n't|[',.?!\)\]])", word.string):
									pass 
								elif word.string=='"':
									if quoting:
										quoting = False
									else:
										s = s + " "
										quoting = True
										skipNextSpace = True
								else:
									if skipNextSpace:
										skipNextSpace = False
									else:
										numwords = numwords + 1
										s = s + " "
							s = s + word.string
							
						# fix & amp ;
						s = re.sub(r"& (\w+) ;", r"&\1;", s);
						# fix ( hello)
						s = re.sub(r"([\(\[]) ", r"\1", s);
						# fix missing final punctuation
						if re.search(r"[\w\d]$", s):
							s = s + "."
						
						senti = sentiment(s);
						sentences.append({'sentiment':senti, 'sentence': s, 'id': tweet.id, 'author': tweet.author})
		
		print numwords
		if not enough:
			enough = (numwords > WORDS_TO_GENERATE)
							
	except SearchEngineLimitError:
		print "Rate limited!"
		enough = True
		
	except Exception as e:
		print "Problem! ", e
		enough = True
	



with io.open('sentences.json', 'w', encoding='utf-8') as f:
  f.write(unicode(json.dumps(sentences, ensure_ascii=False)))

