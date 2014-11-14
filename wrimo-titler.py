# wrimo-titler 
#  - find a title for your novel by stealing from #nanowrimo
# Ranjit Bhatnagar
# for nanogenmo2014
# using pattern from http://www.clips.uantwerpen.be/pattern

from pattern.web import Twitter, SearchEngineLimitError
import re


twitter = Twitter(language='en')

enough = False
firsttime = True
titles = []
byTitle = {}
last = None
i = 0

while not enough:
	try:
	
		if not firsttime:
			sleep(15)
			firsttime = False
		
		for tweet in twitter.search('#nanowrimo title', start=last, count=100):
			i = i + 1
			# look for a tweet containing something in quotes
			last = tweet.id
			match = re.search('(\"[^\"]+\")', tweet.text)
			if match:
				title = {'title':match.group(0), 'author':tweet.author, 'id':tweet.id}
				titles.append(title)
				byTitle[match.group(0)] = title
				
		print i 
		
		if len(byTitle) > 2:
			enough = True
			
	except SearchEngineLimitError:
		print "Rate limited!"
		enough = True
		
	#except Exception as e:
	#	print "Problem! ", e
	#	enough = True
		
#print titles
print "Here's your title - choose one:"
for title, info in byTitle.iteritems():
	print title #, "https://twitter.com/" + info['author'] + "/status/" + info['id']