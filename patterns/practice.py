num = int(input("Enter number: "))
for i in range(1,num):
    for j in range(1,i+1):
        print('*',end="")
    print()    
for i in range(1,num+1):
    for j in range(num,i-1,-1):
        print('*',end="")
    print()    
