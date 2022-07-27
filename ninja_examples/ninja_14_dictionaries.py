# DICTIONARY DATATYPE. Set of Key-value-pairs.
# Just like javascrpt 'object notation'

ninja_belts = {"crystal": "red", "ryu": "black"}
ninja_belts['crystal']
ninja_belts['ryu']

# checking KEYS in DICTIONARIES

'yoshi' in ninja_belts
# getting false
'ryu' in ninja_belts
# getting true

ninja_belts.keys()
# output - dict_keys(['crystal', 'ryu'])
list(ninja_belts.keys())
# output - ['crystal', 'ryu'] a list. much better to work with

# checking VALUES in DICTIONARIES

ninja_belts.values()
list(ninja_belts.values())

vals = list(ninja_belts.values())
vals

# count how many instances are in the list

vals.count('black')
vals.count('orange')

# adding new thingies

ninja_belts['yoshi'] = 'red'
# returns updated dictionary with this new KEY VALUE PAIR
ninja_belts

person = dict(name="shaun", age=27, height="ft")
person


######################################################################

def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt.')


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

ninja_intro(ninja_tails)
