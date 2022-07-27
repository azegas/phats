name = 'shaun'
age = 20
nums = [1, 3, 4, 5]


type(name)
type(age)
type(nums)

# these objects are BASED on those classes

# Docs for str CLASS
# https://docs.python.org/3/library/stdtypes.html


name.count(name)


class Planet:

    def __init__(self):
        # attaching properties to the object
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth System'

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


apple = Planet()               # creating a new instance of 'Planet' class

print(f'Name is: {apple.name}')
print(f'Radius is: {apple.radius}')
print(f'The gravity is: {apple.gravity}')
print(apple.orbit())

planetX = Planet()
