from ninja_18_methods_attributes import Planet

naboo = Planet('naboo', 499999, 8, 'Naboo System')

print(f'Name: {naboo.name}')
print(naboo.spin('a very high speed'))

''' now I have created folder called "space", then added __init__.py
file in it. It is enough to tell python that it is a 'package. Now can
place a couple different files(modules) in it '''


from space.planet import Planet
from space.calc import planet_mass, planet_vol

naboo = Planet('naboo', 499999, 8, 'Naboo System')

naboo.mass = planet_mass(naboo.gravity, naboo.radius)
naboo.vol = planet_vol(naboo.radius)

print(naboo.mass)
print(naboo.vol)

print(f'{naboo.name} has a mass of {naboo.mass} and a volume of {naboo.vol}')
