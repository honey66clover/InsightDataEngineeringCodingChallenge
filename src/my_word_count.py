import sys, os, fnmatch, string, collections

inputdir=sys.argv[1]
outputfiles=sys.argv[2]
punctuations = list(string.punctuation)+["'s"] #punctuations are not counted 
wordcount = {} #dictionary to store the words and the counts
wfile = open(sys.argv[2], 'w') #file to write into the word counts
for file in sorted(os.listdir(inputdir)): #sort the files alphabetically
	if fnmatch.fnmatch(file, "*.txt"): #read all txt files
		rfile = open(inputdir+"/"+file,'r')
		for line in rfile.xreadlines(): #read each line, use xreadlines for big files 
			for punc in punctuations:
				line = line.lower().replace(punc, "") #remove all punctuations			
			for word in line.split():
				#word = word.encode("utf-8-sig") #encode back 
				if word in wordcount:
					wordcount[word] += 1
				else:
					wordcount[word] = 1
		rfile.close()
ordered_wordcount = collections.OrderedDict(sorted(wordcount.items()))
for k,v in ordered_wordcount.items():
	wfile.write(k+"\t"+str(v)+"\n")
wfile.close()
