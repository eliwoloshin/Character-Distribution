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

string = input("Please enter a string of text (the bigger the better): ").lower()
sstring = str.split(string)
letter = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("The distribution of characters in "+string+ " is: ")
for x in alphabet:
    number = string.count(x)
    if number != 0:
        letter.append(x*number)
sortnumber=[]

#letter = list(reversed(sorted(letter, key=len)))
#for x in sorted(letter, key=len, reverse=True):
    #print(x)
#letter.sort()


letter.sort(key=len, reverse=True)
letter.sort()
print(letter)
