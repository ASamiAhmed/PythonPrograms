import csv

with open("first.csv") as f:
  contents_of_file = csv.reader(f)
  
  attendees = []
  for i in contents_of_file:
      attendees.append(i)

print(attendees)
  # for i in range(1,len(attendees)):
  #   printcattendees[i][0])
  
  # with open("first.csv","a") as f:
  #   data = csv.writer(f,delimiter= ",")
  #   data.writerow(["ahmed",0])
