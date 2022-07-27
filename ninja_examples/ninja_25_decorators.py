# cool, wrap a function with other functions. *cough* is a perfect example.
# takes in a function, does something with it, returns it

def cough_dec(func):            # 3 define a decorator

    def func_wrapper():         # 4 make a wrapper
        # code before function
        print('*cough*')
        func()
        # code after function
        print('*cough*')

    return func_wrapper         # 5 return a wrapper

#@cough_dec
@cough_dec                      # 2 add a decorator
def question():                 # 1 describe a function
    print("can you give me a discount on that?")

# question()


# now can apply this decorator to ANY function

@cough_dec
def answer():
    print("it's only 50p you cheapskate")

question()
answer()
