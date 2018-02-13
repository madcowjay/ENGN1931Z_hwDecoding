# Decoding Homework Template Code
#
# This file will query a randomly shifted text string from http://goo.gl/RssCBE.
# This string is loaded as a variable named scambledText and also saved to the file scrambledText.txt
# Your assignment is to programmatically determine the random shift value and then decode the text.
# Pass the decoded text to the variable named unscrambledText, and it will be save to a file unscrambledText.txt
# (It should be clear when you have decoded the text by the output you produce.)
#
# When you have a final answer, you can submit your assignment to the autograde by running the submit.py script

##################################################################
### HELPER CODE TO REQUEST RANDOM SCRAMBLED TEXT STRING FROM WEB
##################################################################
import requests
scrambledText=requests.get("http://goo.gl/RssCBE").text
f1=open('scrambledText.txt','wb')
f1.write(scrambledText.encode('utf8'))
f1.close()

##################################################################
### YOUR CODE TO DECODE AND CORRECT TEXT SHOULD GO BELOW HERE
##################################################################

# import anything else you might need here
import re

email= "jason_webster@brown.edu" #REPLACE THIS
response = requests.get('https://www.gutenberg.org/files/3201/files/COMMON.TXT')
dictionary = response.text
dictionary = dictionary.lower()
splitDictionary = dictionary.split()

shiftedTextArrays = [[] for _ in range(128)]
splitShiftedTextArrays = [[] for _ in range(128)]
print(len(shiftedTextArrays))

scores = [0 for _ in range(128)]

# loop through and build array of arrays of shifted text
print(len(scrambledText))
for i in range(128):
  for j in range(len(scrambledText)):
    shiftedTextArrays[i].append(chr((ord(scrambledText[j])+i)%128))
  shiftedTextArrays[i] = ''.join(shiftedTextArrays[i])
  splitShiftedTextArrays[i] = shiftedTextArrays[i].split()

# rate each word list based on matches to the dictionary
for wordDict in range(len(splitDictionary)):
  for k in range(128):
    for wordShift in range(len(splitShiftedTextArrays[k])):
      if wordDict == wordShift:
        scores[k] = scores[k] + 1

# highest score's index equals the index of the best translation
print(scores)

for l in range(128):
  if scores[l] > 0:
    print(plitShiftedTextArrays[l])



unscrambledText='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER

##################################################################
### HELPER CODE TO SAVE YOUR ANSWER
##################################################################
f2=open('unscrambledText.txt','wb')
f2.write(unscrambledText.encode('utf8'))
f2.close()
##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':'decoding','input':scrambledText,'output':unscrambledText}
