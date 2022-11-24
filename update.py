# mongodb Atlas: https://account.mongodb.com/account/login
# creating a database user: https://docs.atlas.mongodb.com/security-add-mongodb-users/

# Windows : python -m pip install pymongo[srv]
# Linux : sudo pip3 install pymongo[srv]


import pymongo
import json

# defining menue option in a function 
def menu():
    print("1. First Name")
    print("2. Last Name")
    print("3. Address")
    print("4. Email Address")
    print("5. Date of Birth")
    print("6. Grade")
    print("7. Exit")

dbconnection = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.4hubl.mongodb.net/?retryWrites=true&w=majority")
db = dbconnection["StudentRegistrationProject"]
dbcollection = db["StudentInfo"]

#dbcollection.insert_one({"_id": studentId, "firstname:": fname,"lastname:": lname, "email:": email, "address:":address, "dob:":dob})
studentId = int(input('Enter the StudentID of the student that you want to change his/her information: '));
# grade = float(input('Please enter the new grade: '));

menu()
option = int(input('From the menue above select which information you want to update(Enter the number):'))


while option !=7:
    if option==1:
        new_firstName = input('Enter the new First Name: ')
        dbcollection.update_one({"studentId":studentId}, {"$set":{"fname":new_firstName}})
    elif option==2:
        new_lastName = input('Enter the new Last Name: ')
        dbcollection.update_one({"studentId":studentId}, {"$set":{"lname":new_lastName}})  
    elif option==3:
        new_address = input('Enter the new Address: ')
        dbcollection.update_one({"studentId":studentId}, {"$set":{"address":new_address}})
    elif option==4:
        new_email = input('Enter the new Email Address: ')
        dbcollection.update_one({"studentId":studentId}, {"$set":{"email":new_email}})  
    elif option==5:
        new_dob = input('Enter the new Date of Birth: ')
        dbcollection.update_one({"studentId":studentId}, {"$set":{"dob":new_dob}})   
    elif option==6:
        coursename = int(input('Enter the course name: '))
        new_grade = int(input('Enter the new grade: '))
        dbcollection.update_one({"studentId":studentId, "courseInfo.course":coursename }, {"$set":{"courseInfo.$.grade":new_grade}})
        # x = dbcollection.find_one({"studentId":studentId, "courseInfo.course":coursename })
        # print(x["studentId"])
    else:
        input('invalid number')
        
    menu()
    option = int(input("Enter your option:"))
    
if option==7:
   exit()
    
    


