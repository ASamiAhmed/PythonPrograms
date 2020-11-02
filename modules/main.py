from func import addition as add
from func import *



first_no = int(input("Enter first no: "))
second_no = int(input("Enter second no: ")) 
user_input = input('''Which operation do you want to perform? 
Press 1 : Addition
Press 2 : Subtraction
Press 3 : Multiplication
Press 4 : Division
Press 0 : Exit
''')
if user_input== "1":
    returned_value = add(first_no,second_no)
    print(returned_value)
elif user_input== "2":
    returned_value = substract(first_no,second_no)
    print(returned_value)
elif user_input== "3":    
    returned_value = multiply(first_no,second_no)          
    print(returned_value)
elif user_input== "4":    
    returned_value = division(first_no,second_no)          
    print(returned_value)   
else:
    exit()    