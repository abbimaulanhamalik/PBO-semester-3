###Python Local Variables
def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

##Python Global Variables
# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)

###Python Nonlocal Variables
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

