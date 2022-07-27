STR = "hello there dudes"

# SPLIT whenever there is a space
str.split(' ')

fib1 = [1, 1, 2, 3, 4, 8, 13]

fib1

fib1[2]
fib1[5]
fib1[-1]

# SLICINNG from 0 to 4. Including 0 not 4

fib1[0:4]

fib2 = [21, 34, 55]

# CONCATINATING a list - ADDING
fib1 + fib2

# Change the value of one item in the string
fib1[0] = 99

fib1


fib = fib1 + fib2
fib

# APPEND

fib.append(109)
fib

# REMOVE element from array
fib.pop()
fib

fib.append(89)
fib

fib.remove(89)
fib

# DELETE another way
del(fib[4])
fib

# possible, but doesn't make sense
chars = ['mario', 'luigi', 'browser']
chars

chars.append(5)
chars

# list inside a list
nums = [chars, fib1, [1, 2, 3, 4]]
nums
nums[0]
nums[1]
nums[2]
nums

# Get element within WITHIN the list
nums[2][1]
