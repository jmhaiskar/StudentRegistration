import pymongo
import json


# Windows : python -m pip install pymongo[srv]
# Linux : sudo pip3 install pymongo[srv]

dbconnection = pymongo.MongoClient("mongodb+srv://jmhaiskar:aaibaba123@cluster0.sjebylb.mongodb.net")
db = dbconnection["school"]
dbcollection = db["students"]


# Method to enter new student details
def AddStudent():
#    give them a student id
    studentId=10000002
    fname = input("Please enter your first name")
    lname = input("Please enter your last name")
    email= input("Please enter your email")
    address = input("Please enter your address")
    dob = input("Please enter your date of birth") #remember to convert to int
    courseInfo=[]
    courseNum=int(input("How many courses would you like to enter?"))
    
    for i in range(0,courseNum):
            courseName = input("Name of the course: ")
            courseGrade=int(input("What is your grade? "))
            info= {"course" : courseName , "grade" : courseGrade}
            courseInfo.append(info)
                
    dbcollection.insert_one({"studentId": studentId, "fname": fname,"lname": lname, "email": email, "address":address,  "dob":dob, "courseInfo":courseInfo})
   
studentId+=1

    
# Method to delete a student
def DeleteStudent(studentId):
    dbcollection.delete_one({"studentId": studentId})
   

def gradeAssigner():
    courseNum = int(input("How many course to input? "))
    course = []
    sum = 0
    signGrade = ""
    i = {}
    x = []
    for i in range(0,courseNum):
        courseName = input("What is the course name? ")
        grade = float(input("What's your grade? "))
        if(grade<50):
            signGrade = "F"
            course.append(courseName,signGrade)
            x.append(signGrade)
            sum+=0
        elif(grade>=50 and grade<55):
            signGrade = "D"
            course.append(courseName)
            x.append(signGrade)
            sum+=1
        elif(grade>=55 and grade<60):
            signGrade = "C-"
            course.append(courseName)
            x.append(signGrade)
            sum+=1.67
        elif(grade>=60 and grade<65):
            signGrade = "C"
            course.append(courseName)
            x.append(signGrade)
            sum+=2
        elif(grade>=65 and grade<70):
            signGrade = "C+"
            course.append(courseName)
            x.append(signGrade)
            sum+=2.33
        elif(grade>=70 and grade<75):
            signGrade = "B-"
            course.append(courseName)
            x.append(signGrade)
            sum+=2.67
        elif(grade>=75 and grade<80):
            signGrade = "B"
            course.append(courseName)
            x.append(signGrade)
            sum+=3
        elif(grade>=80 and grade<85):
            signGrade = "B+"
            course.append(courseName)
            x.append(signGrade)
            sum+=3.33
        elif(grade>=85 and grade<90):
            signGrade = "A-"
            course.append(courseName)
            x.append(signGrade)
            sum+=3.67
        elif(grade>=90 and grade<95):
            signGrade = "A"
            course.append(courseName)
            x.append(signGrade)
            sum+=4
        elif(grade>=95 and grade<=100):
            signGrade = "A+"
            course.append(courseName)
            x.append(signGrade)
            sum+=4.33
        else:
            print("Invlid input")
        i = {"Courses: ":course, "SignGrades:":x}
        
    
    
    print(i)
    CGpa = sum/courseNum
    print (CGpa)


def show_Report():
    courseName=input("Please enter a Course: ")
    rData = list(dbcollection.find({"courseInfo.course":courseName}).sort("grade", -1).limit(10))
    display(rData)
    
def display(data):
    print (data)


# def UpdateInfo():
#     studentId = int(input('Enter the StudentID of the student that you want to change his/her information: '));

#     menu()
#     option = int(input('From the menue above select which information you want to update(Enter the number):'))


#     while option !=7:
#         if option==1:
#             new_firstName = input('Enter the new First Name: ')
#             dbcollection.update_one({"studentId":studentId}, {"$set":{"fname":new_firstName}})
#         elif option==2:
#             new_lastName = input('Enter the new Last Name: ')
#             dbcollection.update_one({"studentId":studentId}, {"$set":{"lname":new_lastName}})  
#         elif option==3:
#             new_address = input('Enter the new Address: ')
#             dbcollection.update_one({"studentId":studentId}, {"$set":{"address":new_address}})
#         elif option==4:
#             new_email = input('Enter the new Email Address: ')
#             dbcollection.update_one({"studentId":studentId}, {"$set":{"email":new_email}})  
#         elif option==5:
#             new_dob = input('Enter the new Date of Birth: ')
#             dbcollection.update_one({"studentId":studentId}, {"$set":{"dob":new_dob}})   
#         elif option==6:
#             coursename = int(input('Enter the course name: '))
#             new_grade = int(input('Enter the new grade: '))
#             dbcollection.update_one({"studentId":studentId, "courseInfo.course":coursename }, {"$set":{"courseInfo.$.grade":new_grade}})
#         # x = dbcollection.find_one({"studentId":studentId, "courseInfo.course":coursename })
#         # print(x["studentId"])
#         else:
#             input('invalid number')
        
#     menu()
#     option = int(input("Enter your option:"))
    
#     if option==7:
#         exit()
    
    
# def menu():
#     print("1. First Name")
#     print("2. Last Name")
#     print("3. Address")
#     print("4. Email Address")
#     print("5. Date of Birth")
#     print("6. Grade")
#     print("7. Exit")



