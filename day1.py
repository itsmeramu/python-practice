# Simple program to get user's name and age, and determine if they are a minor or adult
name = (input("Enter your name: "))
age = float(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
print(f"Hello, {name}! You are {age} years old.")

# Simple program modulus operation
print(100%2)
print(46%3)

# Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")

#simple program for operators
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)

else:
    print("Invalid operator")