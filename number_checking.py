'''
Write a Python program to check if a number is positive, negative or zero
'''
number = int(input("enter number: "))
if number == 0:
    print("The number you entered is",number)
elif number > 0:
    print("The number you entered is positive")
else:
    print("The number you entered is negative")        