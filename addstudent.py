import csv

mystudent  = {
   "student" : "jawad",
   "student_ID" :  "2095",
   "course" : "software"
    } 
mystudent2  = {
   "student" : "Biden",
   "student_ID" :  "4444",
   "course" : "software"
    } 

studentlist = [mystudent, mystudent2]
mystudent3  = {
   "student" : "Trump",
   "student_ID" :  "33333",
   "course" : "software"
    } 
studentlist.append(mystudent3)
#for item in  studentlist:
 #   print(item["student_ID"])
#with open ("example.txt", "w") as f:
 #for item in  studentlist:
    
def findstudent(name, studentlist):
    for i in studentlist:
        if i["student"] == name:
            print(i)

findstudent("Trump", studentlist)
findstudent("Biden", studentlist)

  #   f.write({item)
