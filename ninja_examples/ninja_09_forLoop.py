ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

for ninja in ninjas:
    print(ninja)

# SLICING

for ninja in ninjas[1:3]:
    print(ninja)


for ninja in ninjas:
    if ninja == 'yoshi':
        print(f'{ninja} - black belt')
        break                   # anything else is not going to cycle throught. get break
    else:
        print(ninja)
