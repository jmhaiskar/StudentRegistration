import pymongo
import json


# Windows : python -m pip install pymongo[srv]
# Linux : sudo pip3 install pymongo[srv]

dbconnection = pymongo.MongoClient("mongodb+srv://jmhaiskar:aaibaba123@cluster0.sjebylb.mongodb.net")
db = dbconnection["sample_geospatial"]
dbcollection = db["shipwrecks"]

# Method to enter new student details
def AddStudent(fname, lname, email, address, dob):
    give them a student id
    fname = input("Please enter your first name")
    lname = input("Please enter your last name")
    email= input("Please enter your email")
#    address = input("Please enter your address")
    dob = input("Please enter your date of birth") #remember to convert to int
#     course=[]
#     courseNum=int(input("How many courses would you like to enter?"))
#             for i in range(0,courseNum):
#                 courseName = input("Name of the course: ")
#                 courseGrade=int(input("What is your grade? "))
#                 info={courseName, courseGrade}
#                 course.append(info)
                
    dbcollection.insert_one({"_id": studentId, "firstname:": fname,"lastname:": lname, "email:": email,  "dob:":dob})
   # "address:":address,
    gradeAssigner()   
                  

    
# Method to delete a student
def DeleteStudent(studentId):
    dbcollection.delete_one({"_id": studentId})
   

def gradeAssigner()
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


