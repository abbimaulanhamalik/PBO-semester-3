###Access and Modify Python Global Variable
c = 1 # global variable

def add():
    print(c)

add()

# Output: 1

# global variable
c = 1 

def add():

     # increment c by 2
    c = c + 2

    print(c)

add()

###Example: Changing Global Variable From Inside a Function using global
# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)

add()

# Output: 3 

