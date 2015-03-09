import sys, os, fnmatch, string, collections
import numpy as np

inputdir = sys.argv[1]
outputfiles = sys.argv[2]
punctuations = list(string.punctuation)+["'s"]
histogram = np.zeros(65536, dtype=np.uint64) #this numpy array is to store the counts of each integer
#the numpy array length = 65536 = 2^16 means the integers should be in range [0,65535]
#the data type uint64 means it can deal with 2^64 = 18446744073709551615 integers at least
total_count = 0 #total numbers of integers, int are automatically promoted to long, no overflow problem

def find_median(histo, count): #given current countings of each integer, return which integer is the median
	sum = 0
	for i in range(0,len(histo)):
		sum += histo[i]
		if sum > (count+1)/2:
			return i
		if sum == (count+1)/2:
			if (count%2==0 and i<len(histo)-1):
				for j in range(i+1,len(histo)):
					if histo[j]>0:
						return float(i+j)/2 #in case of even events
			else:
				return i

wfile = open(sys.argv[2], 'w') #file to write into
for file in sorted(os.listdir(inputdir)): 
	if fnmatch.fnmatch(file, "*.txt"): #read all txt files
		rfile = open(inputdir+"/"+file,'r')
		for line in rfile.xreadlines(): #read each line, xreadlines for big files 
			for punc in punctuations:
				line = line.replace(punc, "") #remove all punctuations			
			wordcount = len(line.split()) #numbers of words per line, on a regular 32bit system, maximum of len() is 536870912			
			total_count += 1
			histogram[wordcount]+=1			
			wfile.write(str(find_median(histogram, total_count))+'\n')
		rfile.close()			
wfile.close()
