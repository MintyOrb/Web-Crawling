# individual project
# Intelligent Systems (ISAT 344)
# 2013.11.3
# 
# PART 2: this code cleans up the scraped data for later analysis


import json

json_file = open ('manipulate.json')
data = json.load(json_file)
json_file.close()


thelist = []

# create new list of dicts with forum name and empty list for the thread titles
for item in data:
	inthere = False
	for things in thelist:
		if things['forumName']==item['name']:
			inthere = True
	if inthere == False:
		thelist.append({'forumName':item['name'],'threadTitles':[]})

# add thread titles to dict item cooresponding to forum name
for item in data:
	for things in thelist:
		if things['forumName'] == item['name']:
			things['threadTitles'].append(item['titles'])

# eliminate duplicates
# approach from stackoverflow answer (string comprehensions):
noDuplicates = [
    {
        'forumName': x['forumName'],
        'threadTitles': list(set(title for lst in x['threadTitles'] for title in lst)) 
    }
    for x in thelist 
]
				 
\

# save to disk
with open("formatted.json" , "wb") as f:
	json.dump(noDuplicates, f)