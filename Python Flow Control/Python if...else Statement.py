###Example: Python if Statement
age = int(input("Enter your age: "))

# Check if age is 18 or more
if age >= 18:
    print("Grant access to the website.")

print("Program complete.")

###Example: Python if…else Statement
age = int(input("Enter your age: "))

if age >= 18:
    print("Grant access.")
else:
    print("Deny access.")

###Example: Authenticate User Logic Using if...else
# Username and password stored in database
username_db = "admin"
password_db = "sparrow@123"

# Username and password entered by the user
username = input("Enter username: ")
password = input("Enter password: ") 

# Check if username & password in database matches user's input
if (username == username_db) and (password == password_db):
    print("Welcome back.")
else:
    print("Access denied.")

###Example: Python if…elif…else Statement
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age >= 18:
    print("Grant access.")
else:
    print("Deny access.")

###Example: Largest of Three Numbers
# Taking input from the user
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

if n1 >= n2 and n1 >= n3:
    largest = n1
elif n2 >= n1 and n2 >= n3:
    largest = n2
else:
    largest = n3

print("The largest number is:", largest)

