# Title: Python 3 Tutorial for Beginners #4 - Strings
# Date: 2022.02.14

'''
42) C-c C-e  = ELPY Edit all occurrences of the symbol at point at once
43) C-c C-c  = ELPY send REGION to python interactive interpreter,
44) C-c C-d  = ELPY show documentation,
45) C-c C-z  = ELPY Switch between your script and the interactive shell
46) M-.      = ELPY go to definition.(or use dumb-jump shortcut M-g g)
47) C-c n/p  = ELPY  move to next, previous error
48) C-c C-v  = ELPY Syntax check with flake8
49) C-c C-n  = ELPY Next flake8 error
50) C-c C-t  = ELPY Start tests
51) C-c RET  = ELPY (new shortcut) evaluate line
'''

# string = sequence of characters. sentence or a word

# no matter what quotes
'hello'
"hello"

"he's a mad man"

'he\'s a mad man'

greet = "hello"
greet

greet[0]
greet[1]
greet[-5]


# SLICING
# first number is inclusive - second is not.
greet[0:3]
greet[2:-1]
# slice all you want - doesn't change the original value
greet
greet = greet[0:3]
greet

greet = 'hello'
str2 = 'dudes'


# CONCATENATION
greet + str2
greet + ' ' + str2


# MULTIPLYING A SRING!
greet * 5


# EVERYTHING IS AN OBJECT IN PYTHON
# so as strings. it has methods. NICE!

greet.capitalize()
greet.upper()
greet
greet = greet.upper()
greet

# SPLITTING
# LIST in a STRING
cheeses = "brie, chedder, stilton"
cheeses.split(',')
cheeses.count('d')
greet
len(greet)
