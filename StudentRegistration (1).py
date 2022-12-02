
import pymongo
import json



# Windows : python -m pip install pymongo[srv]
# Linux : sudo pip3 install pymongo[srv]

dbconnection = pymongo.MongoClient("mongodb+srv://jmhaiskar:aaibaba123@cluster0.sjebylb.mongodb.net")
db = dbconnection["school"]
dbcollection = db["students"]

def main():
    choice=0
    while choice!=7:
        menu()
        choice=int(input("Please select a choice: "))
        
    #     print ("1. Add another student")
    # print ("2. Delete student: ")
    # print ("3. Show student CGPA: ")
    # print ("4. Update student information: ")
    # print ("5. Create report of top 10 student: ")
    # print ("6. Display the student information: ")
    # print ("7. Exit")
        
        if choice==1:
            AddStudent()
        elif choice==2:
            DeleteStudent()
        elif choice==3:
            gradeAssigner()
        elif choice==4:
            UpdateInfo()
        elif choice==5:
            show_Report()
        elif choice==6:
            show_alldata()
        elif choice==7:
            exit()
        else:
            print("invalid selection")
        



# Method to enter new student details
def AddStudent():
#    give them a student id
    #studentId=10000002
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
    result = dbcollection.find().sort("studentId", -1).limit(1)
    dbcollection.insert_one({"studentId": (result[0]["studentId"]+1), "fname": fname,"lname": lname, "email": email, "address":address,  "dob":dob, "courseInfo":courseInfo})
   

    
# Method to delete a student
def DeleteStudent():
    studentId=int(input("Please enter a Student Id: "))
    dbcollection.delete_one({"studentId": studentId})
   

# def gradeAssigner():
#     grade=75
#     studentId= int(input("Please enter a studentId: "))
#     course = db.dbcollection.aggregate([
#                                         {$match :{studentId: "studentId"}},
#                                         {$sum{"courseInfo.grade"}}])
#     #course = list(dbcollection.find({"studentId": studentId, "courseInfo.grade":{$add : ["$grade"]}}))
    
#     print(course)
    # sum = 0
    # signGrade = ""
    # i = {}
    # x = []
    # for i in range(0,courseNum):
    #     courseName = input("What is the course name? ")
    #     grade = float(input("What's your grade? "))
    #     if(grade<50):
    #         signGrade = "F"
    #         course.append(courseName,signGrade)
    #         x.append(signGrade)
    #         sum+=0
    #     elif(grade>=50 and grade<55):
    #         signGrade = "D"
    #         course.append(courseName)
    #         x.append(signGrade)
    #         sum+=1
    #     elif(grade>=55 and grade<60):
    #         signGrade = "C-"
    #         course.append(courseName)
    #         x.append(signGrade)
    #         sum+=1.67
    #     elif(grade>=60 and grade<65):
    #         signGrade = "C"
    #         course.append(courseName)
    #         x.append(signGrade)
    #         sum+=2
    #     elif(grade>=65 and grade<70):
    #         signGrade = "C+"
    #         course.append(courseName)
    #         x.append(signGrade)
    #         sum+=2.33
    #     elif(grade>=70 and grade<75):
    #         signGrade = "B-"
    #         course.append(courseName)
    #         x.append(signGrade)
    #         sum+=2.67
    #     elif(grade>=75 and grade<80):
    #         signGrade = "B"
    #         course.append(courseName)
    #         x.append(signGrade)
    #         sum+=3
    #     elif(grade>=80 and grade<85):
    #         signGrade = "B+"
    #         course.append(courseName)
    #         x.append(signGrade)
    #         sum+=3.33
    #     elif(grade>=85 and grade<90):
    #         signGrade = "A-"
    #         course.append(courseName)
    #         x.append(signGrade)
    #         sum+=3.67
    #     elif(grade>=90 and grade<95):
    #         signGrade = "A"
    #         course.append(courseName)
    #         x.append(signGrade)
    #         sum+=4
    #     elif(grade>=95 and grade<=100):
    #         signGrade = "A+"
    #         course.append(courseName)
    #         x.append(signGrade)
    #         sum+=4.33
    #     else:
    #         print("Invlid input")
    #     i = {"Courses: ":course, "SignGrades:":x}
        
    
    
    # print(i)
    # CGpa = sum/courseNum
    # print (CGpa)


def show_Report():
    courseName=input("Please enter a Course: ")
    rData = list(dbcollection.find({"courseInfo.course":courseName}).sort("grade", -1).limit(10))
    display(rData)
    
def display(data):
    print (data)


def UpdateInfo():
    import Update
    Update
    
# def show():
#     print("StudentID: ", studendId)
#     print("First name: ", fname)
#     print("Last name: ", lname)
#     print("Email address: ", email)
#     print("Date of birth: ", dob)
#     print("Courses:")
#     for i in range(0, len(course)):
#         print(course[i])
        
def show_alldata():
    rData = list(dbcollection.find({}))
    display(rData)

        
def menu():
    print ("1. Add another student")
    print ("2. Delete student: ")
    print ("3. Show student CGPA: ")
    print ("4. Update student information: ")
    print ("5. Create report of top 10 student: ")
    print ("6. Display the student information: ")
    print ("7. Exit")



if __name__ == '__main__':
    main()


