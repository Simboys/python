n=int(input("enter number of student:"))
student={}
for i in range(n):
    rolno=int(input("enter a roll number"))
    name=input("enter student name")
    student[rolno]=name
    print(student)
    
a=int(input("enter a roll number:"))
if a in student:
    print("present")
else:
    print("not present")
