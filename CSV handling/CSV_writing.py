import csv
with open("intro.csv","a") as f:
    bio = csv.writer(f,delimiter=",")
    bio.writerow(["5","warisha","farooq"])
with open("intro.csv","r") as f:
     contents = csv.reader(f) 
     bio = []
     for i in contents:
        bio.append(i)
print(bio)       
    