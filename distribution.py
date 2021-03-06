"""
distribution.py
Author: Eli Woloshin
Credit: http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.
Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string

string = input("Please enter a string of text (the bigger the better): ")
sstring = string.lower()
letter = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print('The distribution of characters in "'+string+ '" is: ')
for x in alphabet:
    letter.append(sstring.count(x))
    
#print(letter)
combin=list(zip(letter, alphabet))
#print(combin)
sortedlist = sorted(combin, key=lambda ew:(-ew[0], ew[1]))
#print(sortedlist)
z=0
while(z<len(alphabet)):
    print(sortedlist[z][0]*sortedlist[z][1])
    z=z+1





    

#for x in sorted(letter, key=len, reverse=True):
   # print(x)
#letter.sort()


#letter.sort(key=len, reverse=True)
#letter.sort()
#print(letter)
