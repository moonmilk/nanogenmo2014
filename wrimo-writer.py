# wrimo-writer 
#  - load tweet files from grabber (could be more than one file in case ran grabber in multiple sessions)
#
# Ranjit Bhatnagar
# for nanogenmo2014

import sys, json
import random, math

# use wrimo-titler to steal a title for your novel
TITLE = "You Can't Write If You Can't Relate"

sentences = []

# load files!
for arg in sys.argv[1:]:
	with open(arg) as jsonfile:
		t = json.loads(jsonfile.read())
		sentences = sentences + t
		print "loading", arg, "with", len(t), "sentences"

print "Total:", len(sentences), "sentences."

wordcount = 0
for sentence in sentences:
	words = sentence['sentence'].split()
	wordcount = wordcount + len(words)
	
print "Total words:", wordcount

# make up some stuff about the book's structure
#   number of chapters - are they long or short?
numchapters = random.randint(6, 23) 
#   number of sentences per chapter
chapterlength = len(sentences) / numchapters
chapterlengthvariation = random.uniform(0.1, 0.2)
#   number of sentences per paragraph
paragraphlength = random.randint(5, 15)
paragraphlengthvariation = random.uniform(0.1, 0.2)


# randomize sentences to get rid of any time correlation
random.shuffle(sentences)

# sort sentences by sentiment
sentences.sort(key = lambda sentence: sentence['sentiment'][0])

# function to retrieve sentences by relative position in list, -1.0 to 1.0
def getsentence(pos):
	if len(sentences) == 0:
		return None
	else:
		i = int((1.0+pos)/2.0 * (len(sentences)-1))
		return sentences.pop(i)


# sentiment arc functions (time from 0.0 to 1.0)
def updownup(t):
	return math.sin(t * 2.5 * math.pi)

def downhill(t):
	return 1.0 - 2.0 * t 

def crashes(t):
	return ((t+0.25) * 3 % 2.0) - 1.0

def uphill(t):
	return 2.0 * t - 1.0


arcs = (updownup, downhill, crashes, uphill)
def randomarc():
	return random.choice(arcs)

# arc of n steps using function f 
def arc(f, n):
	return [f(float(i)/(n-1)) for i in range(0, n)]
		



# title!
print "#", TITLE, "#"
print

bookarc = arc(randomarc(), numchapters)

# chapters!
for c in range(0, numchapters):

	print "##", "Chapter", c+1, "##"
	print
	
	numsentences = int(random.normalvariate(chapterlength, chapterlength * chapterlengthvariation))
	if (numsentences < 1):
		numsentences = 1
	
	chapterarc = arc(randomarc(), numsentences)
	
	while numsentences > 0:
		paragraphindex = 0
		
		paragraphsentences = int(random.normalvariate(paragraphlength, paragraphlength * paragraphlengthvariation))
		if (paragraphsentences < 1):
			 paragraphsentences = 1
		
		paragrapharc = arc(randomarc(), paragraphsentences) 
		
		for s in range(0, paragraphsentences):
			sentiment = (paragrapharc[s] + 2 * chapterarc[paragraphindex] + 2 * bookarc[c]) / 5.0
			
			sentence = getsentence(sentiment)
			if sentence:
				print sentence['sentence'], 
				numsentences = numsentences - 1
			else:
				numsentences = 0
				break;
			
		# paragraph break	
		print
		print
		
	print
	print
	print
	
	if len(sentences) == 0:
		break
		
		

print

# the end!

