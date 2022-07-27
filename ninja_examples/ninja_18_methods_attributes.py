'''
Difference between INSTANCE and CLASS level ATTRIBUTES.
'''

class Planet:                   # CLASS

    shape = 'round'             # CLASS LEVEL ATTRIBUTE, same for all instances, since all the planets are round

    def __init__(self, name, radius, gravity, system):  # INSTANCE OF A CLASS
        # attaching properties to the object
        self.name = name        # INSTANCE attribute
        self.radius = radius    # INSTANCE attribute
        self.gravity = gravity  # INSTANCE attribute
        self.system = system    # INSTANCE attribute

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'  # INSTANCE METHOD

    # METHOD that is common for ALL planets
    # cls - has access to all the class and its attributes

    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    # only has access to the parameters that we set individually
    @staticmethod
    def spin(speed = "200 miles per hour"):  # setting with default parameters
        return f'The planet spins and spins at {speed}'


apple = Planet('Hoth', 200000, 5.5, 'Hotttt System')

print(f'Name is: {apple.name}')
print(f'Radius is: {apple.radius}')
print(f'The gravity is: {apple.gravity}')
print(apple.orbit())

# so far the output is the same as in the previous tutorial. We Just
# changed a few things, but output is the same.

# NOW we are CREATING NEW INSTANCE

naboo = Planet('naboo', 499999, 8, 'Naboo System')
print(f'Name is: {naboo.name}')
print(f'Radius is: {naboo.radius}')
print(f'The gravity is: {naboo.gravity}')
print(apple.orbit())

print(Planet.shape)             # 1. Class itself + class level attribute
print(naboo.shape)              # 2. Instance has access to class
                                # level attributes as well

# print(Planet.name)              # name and so on are INSTANCE
                                # ATTRIBUTES, only apply to individual
                                # INSTANCES when we create a new
                                # planet

print(Planet.commons())         # this thingy is available in planets
print(naboo.commons())          # AND in instance
print(Planet.spin())            # works
print(Planet.spin('a very high speed'))            # overriding default value

print(naboo.spin('a very high speed'))            # naboo also works
