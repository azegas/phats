my_name = 'ryu'                 # GLOBAL scope variable


def print_name():
    my_name = 'bob'
    print('the name inside the function is', my_name)


print_name()

print('outside the function the name is', my_name)
