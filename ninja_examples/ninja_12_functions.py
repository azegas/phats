# DECIDING THE VARIABLES OURSELVES

def greet(name, time):
    print(f'Good {time}, {name}, hope you are well!')


greet('Arvydas', 'morning')

# SETTING DEFAULT PARAMETERS


def greet2(name='ryu', time='morning'):
    print(f'Good {time}, {name}, hope you are well!')


greet2()

# ASKING THE USER FOR THEIR NAME AND TIME OF DAY

def greet2(name, time):
    print(f'Good {time}, {name}, hope you are well!')


name = input('enter your name: ')
time = input('enter the time of day: ')

greet2(name, time)

# FUNCTION THAT CALCULATES THE AREA AND VOLUME OF A CIRCLE


def area(radius):
    return 3.142 * radius * radius


def vol(area, length):
    print(area * length)


radius = int(input('enter a radius: '))
length = int(input('enter a length: '))

area_calc = area(radius)
vol(area_calc, length)
###############################################################################

# MY OWN PRACTICE

################################################################################

# Perimeter of rectangle = 2 (length + width)

def perimeter(length, width):
    print(2 * (length + width))

length = int(input('enter length: '))
width = int(input('enter width: '))

perimeter(length, width)

# Perimeter of a square

def square_perimeter(krastine):
    print(4*krastine)

krastine = int(input('enter krastine: '))

square_perimeter(krastine)

# area of a square

def square_area(krastine):
    print(krastine * krastine)

krastine = int(input('enter krastine: '))

square_area(krastine)

# The volume of cuboid

def vol_cuboid(length, width, height):
    return length, width, height

length = int(input('enter length: '))
width = int(input('enter width: '))
height = int(input('enter height: '))

vol_cuboid(length, width, height)
print(length *  width * height)
