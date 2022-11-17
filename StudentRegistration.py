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
    address = input("Please enter your address")
    dob = input("Please enter your date of birth") #remember to convert to int
    course=[]
    courseNum=int(input("How many courses would you like to enter?"))
            for i in range(0,courseNum):
                courseName = input("Name of the car: ")
                course.append(carName)
                
            
                  
    dbcollection.insert_one({"_id": studentId, "firstname:": fname,"lastname:": lname, "email:": email, "address:":address, "dob:":dob})
    
# Method to delete a student
def DeleteStudent(studentId):
    dbcollection.delete_one({"_id": studentId})
    
    post={"studentId":0, "firstname:": "Josh","lastname:": "Lomeli"}    
    dbcollection.insert_one(post)

#dbcollection.delete_one("studentId": studentId)

def gradeAssigner()
    grade = float(input("What's your grade? "))
    gpa = 0.0
    if(grade<50):
        signGrade = "F"
        gpa = 0
    elif(grade>=50 && grade<55):
        signGrade = "D"
        gpa = 1
    elif(grade>=55 && grade<60):
        signGrade = "C-"
        gpa = 1.67
    elif(grade>=60 && grade<65):
        signGrade = "C"
        gpa = 2
    elif(grade>=65 && grade<70):
        signGrade = "C+"
        gpa = 2.33
    elif(grade>=70 && grade<75):
        signGrade = "B-"
        gpa = 2.67
    elif(grade>=75 && grade<80):
        signGrade = "B"
        gpa = 3
    elif(grade>=80 && grade<85):
        signGrade = "B+"
        gpa = 3.33
    elif(grade>=85 && grade<90):
        signGrade = "A-"
        gpa = 3.67
    elif(grade>=90 && grade<95):
        signGrade = "A"
        gpa = 4
    elif(grade>=95 && grade<100):
        signGrade = "A+"
        gpa = 4.33
    else:
        print("Invlid input")


