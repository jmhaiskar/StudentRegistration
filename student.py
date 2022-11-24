# mongodb Atlas: https://account.mongodb.com/account/login
# creating a database user: https://docs.atlas.mongodb.com/security-add-mongodb-users/

# Windows : python -m pip install pymongo[srv]
# Linux : sudo pip3 install pymongo[srv]


import pymongo
import json

dbconnection = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.4hubl.mongodb.net/?retryWrites=true&w=majority")
db = dbconnection["StudentRegistrationProject"]
dbcollection = db["StudentInfo"]

# Method to enter new student details
#def add(fname, lname, email, address, dob):
studentId=0
    #fname, lname, email, address, dob
    #give them a student id
    #dbcollection.insert_one({"_id": studentId, "firstname:": fname,"lastname:": lname, "email:": email, "address:":address, "dob:":dob})
post={"studentId":100245077, "fname": "jay","lname": "prit","address":"westvan","email": "123jay@gmail.com","dob":"04-04-1970", "courseInfo" : [{"course" : 1170 , "grade" : 80},{"course" : 1240 , "grade" : 50}]}    
dbcollection.insert_one(post)