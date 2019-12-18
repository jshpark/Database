import sqlite3
from Student import Student

connection = sqlite3.connect('StudentDB')
c = connection.cursor()


class Simulation:


    def startProgram(self):
        print("1) Display all students and their attributes.")
        print("2) Create student")
        print("3) Update Student")
        print("4) Delete Student")
        print("5) Search/Display Students by Major, GPA, and Advisor")
        print("6) Exit")


        while(True):
            try:
                choice = int(input("Enter a valid option: "))
            except:
                print("Please enter a number.")
            else:
                break

        return choice


    def choiceOne(self):
        c.execute("SELECT * FROM Student")
        for row in c.fetchall():
            print(row)

    def choiceTwo(self):
        first_name = input("Enter their first name: ")
        last_name = input("Enter their last name: ")
        gpaCheck = True
        while (gpaCheck):
            try:
                gpa = float(input("Enter their GPA: "))
            except:
                print("Please enter a valid GPA")
            else:
                gpaCheck = False
        major = input("Enter their major: ")
        facultyadv = input("Enter their faculty advisor: ")
        stu = Student(first_name, last_name, gpa, major, facultyadv)
        c.execute("INSERT INTO Student('FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor')"
                  "VALUES (?, ?, ?, ?, ?)", stu.getStudentTuple())
        connection.commit()

    def choiceThree(self):
        checkID = True
        while (checkID):
            try:
                studentID = int(input("Enter desired student's ID: "))
            except:
                print("Please enter an ID")
            else:
                checkID = False

        checkExistID = True
        while (checkExistID):
            c.execute("SELECT StudentID FROM Student")
            existID = False
            for row in c.fetchall():
                if (studentID == row[0]):
                    existID = True
                    break
            if (existID == False):
                print("Student does not exist. Please enter an existing ID: ")
                studentID = int(input())
            else:
                checkExistID = False
        #ID now exists, so now we can update
        newMajor = input("Enter student's new major: ")
        newAdvisor = input("Enter student's new advisor: ")

        sql = "UPDATE Student SET Major = ?, FacultyAdvisor = ? WHERE StudentID = ?"
        val = (newMajor, newAdvisor, studentID)
        c.execute(sql, val)
        connection.commit()

    def choiceFour(self):
        checkID = True
        while (checkID):
            try:
                studentID = int(input("Enter desired student's ID: "))
            except:
                print("Please enter an ID")
            else:
                checkID = False

        checkExistID = True
        while (checkExistID):
            c.execute("SELECT StudentID FROM Student")
            existID = False
            for row in c.fetchall():
                if (studentID == row[0]):
                    existID = True
                    break
            if (existID == False):
                print("Student does not exist. Please enter an existing ID: ")
                studentID = int(input())
            else:
                checkExistID = False
        #id exists, so now we can delete the tuple

        sql = "DELETE from Student WHERE StudentID = ?"
        val = (studentID, )

        c.execute(sql, val)
        connection.commit()

    def choiceFive(self):
        print("1) Major")
        print("2) GPA")
        print("3) Advisor")
        print("Please input the corresponding option.")

        userChoiceBool = True
        while (userChoiceBool):
            try:
                userChoice = int(input("How would you like to search the students?: "))
            except:
                print("Please insert a number.")
            else:
                userChoiceBool = False

        while (True):
            if ((userChoice == 1) or (userChoice == 2) or (userChoice == 3)):
                break
                #option is valid
            else:
                try:
                    userChoice = int(input("Please enter a valid option: "))
                except:
                    print("Please insert a number.")
                    userChoice = int(input("Please enter a valid option: "))

        #CHOICE IS VALID
        if (userChoice == 1):
            major = input("What major would you like to search by?: ")

            checkExistMajor = True
            while (checkExistMajor):
                c.execute("SELECT Major FROM Student")
                existMajor = False
                for row in c.fetchall():
                    if (major == row[0]):
                        existMajor = True
                        break
                if (existMajor == False):
                    print("Major does not exist. Please enter an existing major: ")
                    major = (input())
                else:
                    checkExistMajor = False
            #major exists in the table
            sql = ("SELECT * FROM Student WHERE Major = ?")
            val = (major, )
            c.execute(sql, val)
            for row in c.fetchall():
                print(row)

        elif (userChoice == 2):
            gpaCheck = True
            while (gpaCheck):
                try:
                    gpa = float(input("Enter their GPA: "))
                except:
                    print("Please enter a valid GPA")
                else:
                    gpaCheck = False
            #now we must check if the GPA exists in the table
            checkExistGPA = True
            while (checkExistGPA):
                c.execute("SELECT GPA FROM Student")
                existGPA = False
                for row in c.fetchall():
                    if (gpa == row[0]):
                        existGPA = True
                        break
                if (existGPA == False):
                    print("GPA does not exist. Please enter an existing GPA: ")
                    gpa = float(input())
                else:
                    checkExistGPA = False
            #gpa exists, now we print
            sql = ("SELECT * FROM Student WHERE GPA = ?")
            val = (gpa,)
            c.execute(sql, val)
            for row in c.fetchall():
                print(row)

        elif (userChoice == 3):
            advisor = input("Which advisor would you like to search by?: ")

            checkExistAdvisor = True
            while (checkExistAdvisor):
                c.execute("SELECT FacultyAdvisor FROM Student")
                existAdvisor = False
                for row in c.fetchall():
                    if (advisor == row[0]):
                        existAdvisor = True
                        break
                if (existAdvisor == False):
                    print("Major does not exist. Please enter an existing major: ")
                    advisor = (input())
                else:
                    checkExistAdvisor = False
            # major exists in the table
            sql = ("SELECT * FROM Student WHERE FacultyAdvisor = ?")
            val = (advisor,)
            c.execute(sql, val)
            for row in c.fetchall():
                print(row)

    def choiceSix(self):
        return False






