###Example: Infinite while Loop
number = float(input("Enter a number: "))

while number >= 0.0:
    print(number)

###Example: Finite while Loop
number = float(input("Enter a number: "))

while number >= 0.0:
    print(number)
    
    # Take number input again
    number = float(input("Enter another number: "))

###Example: Print Numbers from 1 to n
n = 10
i = 1

while i <= n:
    print(i)
    i += 1 

###Example: Sum Numbers Until User Enters Zero
total = 0
n = float(input("Enter a number (0 to stop): "))

while n != 0.0:
    total += n
    n = float(input("Enter a number (0 to stop): "))

print(f"Sum: {total}")

