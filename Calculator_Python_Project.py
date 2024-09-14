# Write a Python program to build a simple Calculator
"""
Available operations
    1. Addition - sum of multiple numbers
    2. Subtraction - Difference btw 2 numbers
    3. Multiplication - Product of multiple numbers
    4. Division - Quotient of 2 numbers
    5. Average - Average of multiple numbers
"""
# 3 steps to build calculator
#   1. Create functions needed
#   2. User input
#   3. Print result

# Step-1 Create Functions

# Add function
def add(num1,num2):
    return num1 + num2

# Subtract function
def sub(num1,num2):
    return num1 - num2

# Multiply function
def multiply(num1,num2):
    return num1 * num2

# Divide function
def div(num1,num2):
    return num1 / num2

# Average function
def avg(num1,num2):
    return (num1 + num2) / 2

# Step-2 User Input
print("")

print("Welcome To Calculator")

number1 = int(input("Enter First number: "))
number2 = int(input("Enter Second number: "))

print("")

print("Please select a operation:\n" \
    "1. Addition\n" \
    "2. Subtration\n" \
    "3. Multiply\n" \
    "4. Division\n" \
    "5. Average\n")

select = int(input("Select a operation from 1,2,3,4,5: "))

print("")
# Step-3 Print the result

if select == 1:
    print(F"Sum => {number1} + {number2} = {add(number1,number2)}")
elif select == 2:
    print(F"Minus => {number1} - {number2} = {sub(number1,number2)}")
elif select == 3:
    print(F"Multiply => {number1} * {number2} = {multiply(number1,number2)}")
elif select == 4:
    print(F"Division => {number1} / {number2} = {div(number1,number2)}")
elif select == 5:
    print(F"Avg => ({number1} + {number2})/2 = {avg(number1,number2)}")
else:
    print("Invalid operation! Pls select again!")

print("")
