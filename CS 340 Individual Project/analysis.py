# individual project
# Intelligent Systems (ISAT 344)
# 2013.11.3
# 
# PART 3: this script performs analysis on data formatted in part 2.

import json
from textblob import TextBlob

json_file = open ('formatted.json')
data = json.load(json_file)
json_file.close()

stopWords = ['the','is', '\'s', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']

# loop through all dictionaries in data, preform anlysis on each and print results
for items in data:

	string = ""
	stringNoStops = ""

	#count threads per forum
	count = 0
	for titles in items['threadTitles']:
		count += 1
	items['numberOfThreads'] = count

	print ""
	print "Forum Name: ",
	print items['forumName']
	print "Number of Threads: ",
	print items['numberOfThreads']

	# make thread titles array into a single string
	for titles in items['threadTitles']:
		string += " " + titles

	# set value in dict list for later storage
	# items['titlesString'] = string

	string = string.lower()

	# remove stopwords - from stackoverflow: http://stackoverflow.com/questions/9953619/technique-to-remove-common-wordsand-their-plural-versions-from-a-string
	listNoStops = filter(lambda w: not w in stopWords, string.split())

	# remove words less than two characters in length (to prevent getting 'no substring' error)
	for word in listNoStops:
		if len(word) > 2:
			stringNoStops += " " + word

	# get count of words in the string using TextBlob
	blob = TextBlob(stringNoStops)
	allWords = blob.words
	
	# eliminate duplicates from allWords
	wordSet = set(allWords)

	# initialize top list
	topWords = [{'occurrances':0,'word':'iniital'}]

	# determine top words and occurrances in current forum
	for word in wordSet:
		# get occurrances for each word in topWords
		listOfValues = [x['occurrances'] for x in topWords]
		# if the new word appears more than the lowest occurance in topWords, add it
		if blob.words.count(word) > min(listOfValues):
			topWords.append({'occurrances':blob.words.count(word),'word':word})
			# if topWords has more than 10 values in it, delete the item with the lowest value
			if len(topWords) > 10:
				place = topWords.index(min(topWords))
				del topWords[place]

	# sort the topList based on occurrances and print
	topWords = sorted(topWords, key=lambda k: k['occurrances']) 
	for word in topWords:
		print "Word: ",
		print word['word'],
		print " occurrances: ",
		print word['occurrances']

				








