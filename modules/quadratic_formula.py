import math

def quadratic(a,b,c):
    return (-b+(math.sqrt(b**2)-(4*a*c))/(2*a) )
a = int(input("enter your number..."))
b = int(input("enter your number..."))
c = int(input("enter your number..."))

if a==0:
    print("invalid input")
else:
    returned_value = quadratic(a,b,c)    
    print(returned_value)