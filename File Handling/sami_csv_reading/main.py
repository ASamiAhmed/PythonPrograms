import csv

with open("first.csv") as f:
  contents_of_file = csv.reader(f)
  
  attendees = []
  for i in contents_of_file:
    attendees.append(i)


for i in range(1,len(attendees)):
  print(attendees[i][0])