#!/usr/bin/python
import sys
arg1=sys.argv[1]
arg2=sys.argv[2]
def searchString(string=arg1, fileName=arg2):
	f=fileName
	myFile = open(f)
	myString=string
	l=[]
	n=0
	print "The string: '" + myString + "' was founded in lines: "
	for line in myFile:
        	n+=1
        	if myString in line:
            		l.append(n)
    	print l 
searchString()


