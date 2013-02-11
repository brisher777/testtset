#!/usr/bin/python

import time
import subprocess
import os

#read from STDIN
#convert it to a list
#each char in the list gets compared to data parsed from a parsed curl

######
######
######IMPORTANT: to do this properly, each time it finds a match, that match needs to be output to a file
######		 and added into the curl statement for the next iteration, so they match up
######		 could do it manually, but loses some pizazz
######		 -- how do i read in from a file --
######		 -- how do i create and then append a file --
######
######

def two_position(to_encode):
	#print to_encode
	#time.sleep(3)
	char = 0
	#while new_variable != to_encode
	#new_variable = curl()
	#check this for logic error
	
	while char != ord(to_encode):
		a = str(chr(char)).encode("hex")
		#insert curl call here, can pass 'a' to it
		#in the curl call, use curl and parse the data
		#make the return'd character what is used for comparison 
		#in this function
		char = char + 1
		if ord(to_encode) == char:
			#print "found it fucker, char is:" + str(chr(char)).encode("hex")
			#print "encode is:" + to_encode
			f = open('junk', 'a+')
			f
			f.write(str(chr(char)).encode("hex"))
			f.seek(0, os.SEEK_SET)
			f.readline()
		#print "testing with: %s" %(a)
		#time.sleep(0.1)
		if char == 256:
			char = 0
			#time.sleep(5)
			third_position(to_encode, char)

def third_position(to_encode, byte):
	char = 0
	#first halfbyte
	for x in range(16):
		a = str(chr(char)).encode("hex")
		char = char + 1
		#print "testing third with: %s" %(a)
		for y in range(256):
			b = str(chr(byte)).encode("hex")
			byte = byte + 1
			print "testing all with: %s" %(a.lstrip('0') + b)
			if to_encode == a.lstrip('0') + b:
				print "found it fucker"
		byte = 0
			
#two_position(0)
def curl():
	#curl statement here, a from two_position will be passed to this function
	#curl will occur once
	#curl data will be redirected to a file for parsing
	#grep will parse the data
	grep = subprocess.Popen(["cat /home/ben/testtset/testgrep | grep code | tr -s '<,>, ' ':' | cut -d : -f 11"], stdout=subprocess.PIPE, shell=True)
	(out, err) = grep.communicate()
	return out ## out returns one character back to two_position for comparison
	#if grep is problematic, can try paring it down to a manageable list 
	#and then calling the appropriate array number from there
	#for i in range(len(list(out.strip()))):
		#two_position(out[i])
	
to_encode = list(raw_input("Enter what you want checked against the server's response: ").strip())
for i in range(len(to_encode)):
	two_position(to_encode[i])	
	
	

