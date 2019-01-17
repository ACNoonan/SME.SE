#Initial code found at: http://aakashjapi.com/fuckin-search-engines-how-do-they-work/

#First step is coded to parse & tokenize our documents.

#Steps are as follows:
#	1. Remove all punctuation & Split on whitespace. (def process_files)
#	2. Create a temporary hashtable that maps filenames to their list of tokens.

def process_files(filenames):
	file_to_terms = {}
	for file in filenames:
		pattern = re.compile('[\W_]+')
		file_to_terms[file] = open(file, 'r').read().lower();
		file_to_terms[file] = pattern.sub(' ',file_to_terms[file])
		re.sub(r'[\W_]+','', file_to_terms[file])
		file_to_terms[file] = file_to_terms[file].split()
	return file_to_terms



#Two additional steps are suggested that aren't already in place:
#	1. Removing all stopwords (words like "the", "and", "a", etc.)
#	2. Stemming all the words (so that "running", "runner" & "runs" become "run")



#input = [word1, word2, ...]
#output = {word1: [pos1, pos2], word2: [pos2, pos434], ...}
#Define this process.
def index_one_file(termlist):
	fileIndex = {}
	for index, word in enumerate(termlist):
		if word in fileIndex.keys():
			fileIndex[word].append(index)
		else:
			fileIndex[word] = [index]
	return fileIndex
	
	
	
#input = {filename: [word1, word2, ...], ...}
#res = {filename: {word: [pos1, pos2, ...]}, ...}
#Define this process.
def make_indices(termlists):
	total = {}
	for filename in termlists.keys():
		total[filename] = index_one_file(termlists[filename])
	return total



#input = {filename: {word: [pos1, pos2, ...], ... }}
#res = {word: {filename: [pos1, pos2]}, ...}, ...}
#Define this process. (Creates the inverted index?)

def fullIndex(regdex):
	total_index = {}
	for filename in regdex.keys():
		for word in regdex[filename].keys():
			if word in total_index.keys():
				if filename in total_index[word].keys():
					total_index[word][filename].extend(regdex[filename][word][:])
				else:
					total_index[word][filename] = regdex[filename][word]
			else:
				total_index[word] = {filename: regdex[filename][word]}
	return total_index
	
	#LEFT OFF @ QUERYING THE INDEX
