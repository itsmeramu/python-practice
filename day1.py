name = (input("Enter your name: "))
age = float(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
print(f"Hello, {name}! You are {age} years old.")