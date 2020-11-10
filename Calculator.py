def addition(first_no,second_no):
    return (first_no + second_no)
def substract(first_no,second_no):
    return (first_no - second_no)
def multiply(first_no,second_no):
    return (first_no * second_no)
def division(first_no,second_no):
    if second_no == 0:
        print("invalid input")
    else:
        return(first_no / second_no)    
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
    returned_value = addition(first_no,second_no)
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