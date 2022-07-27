# Title: Python 3 Tutorial for Beginners #3 - Numbers
# Date: 2022.02.13

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

'''
Imagine a real life OBJECT - car.
It has ATTRIBUTES that describe the car: size, color, speed,
It has FUNCTIONS : drive, brake, accelerate, reverse, etc.

Same in python. Everything is an OBJECT and every object has
ATTRIBUTES and FUNCTIONS(or methods).
To find out what kind of object it is, use "type()"
'''

type(5)                         # integer
type(3.4)                       # float
5+5
5-5
5*5
5/5                             # returns float, not an integer! Python3 thingy
5//5                            # oplia, returns integer
2**2                            # square
10 % 3                          # % =  modulus. 10/3 - 1 is left. 1 =  modulus
5+5*3                           # =20
# BIDMAS                        # brackets, square, division, multiplication, addition, subtraction
(5+5)*3

# VARIABLES
age = 25
age
age + 5                         # doesnt chagne age value
age = age + 5                   # now added to age value
age
age += 5                        # prideda prie age.
age
age -= 5                        # ateima is age
age
age /= 2
age
age //= 2
age

wages = 1000
bills = 200
rent = 500
food = 200

savings = wages - bills - rent - food
savings
print("My savings are " + str(savings))
