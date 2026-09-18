###Example: Python Function Call
def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')

###Python Function Arguments
def greet(name):
    print("Hello", name)

# pass argument
greet("John")

###Example: Function to Add Two Numbers
# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)

###The return Statement
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)

###The pass Statement
def future_function():
    pass

# this will execute without any action or error
future_function()  

###Example: Python Library Function
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)

###