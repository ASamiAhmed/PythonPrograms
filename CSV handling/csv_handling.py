import csv
with open("intro.csv","r") as f:
    contents = csv.reader(f)
    bio = []   
    for i in contents:
        bio.append(i) 
print(bio)    
for i in range(0,len(bio)):
    print(bio[i][2])  