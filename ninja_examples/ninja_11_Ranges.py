# plural = [1,2,3,4,5]

# for singular in plural:
#     # do something


for n in range(5):
    print(n)


# First point - inclusive
# second point - not inclusive
for n in range(3, 10):
    print(n)


# third argument - step size
for n in range(0, 20, 4):
    if n == 0:
        n += 1
        continue
    print(n)


burgers = ['beef', 'chicken', 'veg', 'supreme', 'double', 'max']


for n in range(len(burgers)):
    print(n, burgers[n])


# Reverse
for n in range(len(burgers)-1, -1, -1):
    print(n, burgers[n])
