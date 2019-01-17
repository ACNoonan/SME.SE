 #Additional steps are suggested that aren't already in place:
 #	1. Stemming query words
 #	2. Make everything .lower()
 #	3. Remove puntuation
 
 #Starting with Standard Queries (One Word):
 def one_word_query(word, invertedIndex):
	pattern = re.compile('[\W_]+')
	word = pattern.sub(' ',word)
	if word in invertedIndex.keys():
		return [filename for filename in invertedIndex[word].keys()]
	else:
		return []
		


#Aggregate lists & union them:
#Option: If we want a query that ensures that every word in the query
#		 shows up in the final results list, use an intersection instead
#		 of a union.

def free_text_query(string):
	pattern = re.compile('[\W_]+')
	string = pattern.sub(' ',string)
	result = []
	for word in string.split():
		result += one_word_query(word)
	return list(set(result))
	


#Phrase Queries
#Steps:
#	1. Sanitizes the input.
#	2. Runs a single word query for every word in input.
#	3. Each of these results is added to a list.
#	4. Create a set called 'setted'. This takes an intersection of
#			first list with all other lists, leaving the intermediate 
#			result:	documents containting input/query.
#	5. Create a list of every document in intermediate results.
#	6. 2 Nested for loops iterate this list:
#			A) Goes through every list and subtracts an iterative '-i'
#				from each list (creating an equal-value for phrases)
#			B) Take an intersection of these lists to find matching phrases.
def phrase_query(string, invertedIndex):
	pattern = re.compile('[\W_]+')
	string = pattern.sub(' ',string)
	listOfLists, result = [],[]
	for word in string.split():
		listOfLists.append(one_word_query(word))
	setted = set(listOfLists[0]).intersection(*listOfLists)
	for filename in setted:
		temp = []
		for word in string.split():
			temp.append(invertedIndex[word][filename][:])
		for i in range(len(temp)):
			for ind in range(len(temp[i])):
				temp[i][ind] -= i
		if set(temp[0]).intersection(*temp):
			result.append(filename)
	return rankResults(result, string)

 
