num = int(input("enter num: "))
for i in range(1,num):
    for j in range(1,i+1):
        print('*',end="")
    print()
for i in range(1,num+1):
    for k in range(num,i-1,-1):
        print('*',end="")
    print()