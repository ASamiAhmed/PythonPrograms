#Write a Python program to get the difference between a given number and
#17, difference cannot be negative
number = int(input("enter number: "))
if number>17:
    print("please input no. less than 17")
else:
    answer = 17 - number
    print(answer)