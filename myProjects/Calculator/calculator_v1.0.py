# A Simple Calculator

# Getting first number from the user.
num1 = input("Enter a number: ")

# Getting second number from the user.
num2 = input("Enter another number: ")

# Building menu for operations.
print("Operation Keys:\na - Add\ns - Subtract\nm - Multiplication\nd - Division")

# Getting operation input from the user.
operation = input("Kindly select an operation key: ")

# Using if-else condition to satisfy operation condition
if operation == "a":
    result = float(num1) + float(num2)
    print(round(result))

elif operation == "s":
    result = float(num1) - float(num2)
    print(round(result))

elif operation == "m":
    result = float(num1) * float(num2)
    print(round(result))

elif operation == "d":
    result = float(num1) / float(num2)
    print(round(result))

else:
    print("Option " + operation + " is not available.")
