import csv
name = input("enter your name: ")
father_name = input("enter your father name: ")
age =int(input("enter your age: "))
grade =input("enter your grade: ")
height =float(input("enter your height: "))
with open("bio.csv","w") as f:
    intro = csv.writer(f,delimiter=",")
    intro.writerow(["name","father_name","age","grade","height"])
    intro.writerow([name,father_name,age,grade,height])