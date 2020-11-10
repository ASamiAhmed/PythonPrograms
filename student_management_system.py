import csv
user_input =int(input('''which operation do you want to perform?
Press_1: Write
Press_2: Read
Press_0: Exit
'''))
if user_input==1: 
    name = input("enter your name: ")
    father_name = input("enter your father name: ")
    age =int(input("enter your age: "))
    grade =input("enter your grade: ")
    height =float(input("enter your height: "))
    with open("bio.csv","w",newline='') as f:
        intro = csv.writer(f,delimiter=",")
        intro.writerow(["name","father_name","age","grade","height"])
        intro.writerow([name,father_name,age,grade,height])
        print('information submitted')  
    
if user_input==2:
    with open("bio.csv") as f:
        bio = csv.reader(f)
        empty=[]
        for i in bio:
            empty.append(i)
    print(empty)
if user_input==0:
    exit()            




