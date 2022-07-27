class Planet:
    def __init__(self, name, radius, gravity, system):
        # attaching properties to the object
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


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
