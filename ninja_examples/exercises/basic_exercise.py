# resource - https://www.w3resource.com/python-exercises/python-basic-exercises.php#EDITOR

#  1. Write a Python program to print the following string in a
# specific format (see the output).

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# 2. Write a Python program to get the Python version you are using.

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

# 3. Write a Python program to display the current date and time.

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# 4. Write a Python program which accepts the radius of a circle from
# the user and compute the area.


r = 1.1
pi = 3.14159265359

print(pi*(r*r))
print(pi * r**2)

# OR this sulution

from math import pi
r = float(input("Input the radius of the circle : "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# 5. Write a Python program which accepts the user's first and last
# name and print them in reverse order with a space between them.

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
