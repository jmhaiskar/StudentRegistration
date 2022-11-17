

def main():
    
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
    
if __name__ == '__main__':
    main()