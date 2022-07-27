# LISTS

nums = [1,9, 56, 3,5,6,7,7,5]
sorted(nums)

# capital letters ALWAYS COME FIRST! Attention!
names = ['shaun', 'ryu', 'Arvydas', 'antanas', 'Brian', 'shaun']
sorted(names)


# SETS
# do not allow duplicates

set(nums)                       # takes out all duplicates
set(names)                      # removed duplicates AND messed up the order


# DICTIONARY
ninjas = {'ryu': 'black', 'yoshi': 'red', 'antanas': 'black'}
set(ninjas)
ninjas.values()
set(ninjas.values())            # taking out duplicates of the dictionary, cool


##################################### FROM LAST TUTORIAL

def belt_count(dictionary):
    belt = list(dictionary.values())
    for belt in belts:
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

# def ninja_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f'I am {key} and I am a {val} belt.')


ninja_tails = {}                # this will become a "dictionary" after we put in the values

while True:
    ninja_name = input('enter a ninja name: ')  # key
    ninja_belt = input('enter a belt color: ')  # value
    ninja_tails[ninja_name] = ninja_belt

    another = input('add another? (y/n) ')
    if another == 'y':
        continue                # go back to the top of the loop and start again
    else:
        break                   # break out of this loop

# ninja_intro(ninja_tails)
belt_count(ninja_belt)
