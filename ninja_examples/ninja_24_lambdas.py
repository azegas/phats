# a function that doesn't have a name, it doesn't have to, because it
# is being called only once.

# use them in line

nums = [1,2,3,4,5]

def square(n):
    return n * n

print(list(map(square, nums)))
print(list(map(lambda z: z*z, nums)))
