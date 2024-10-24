#input
grade = int(input("Enter your grade: "))
gpa = float(input("Enter your GPA:"))
gender = input("Enter your gender")

#process
if (gpa >= 3.5) and (grade == 10) or (grade == 11):
# if (gpa >= 3.5) and (grade > 9 and grade < 12)
# if gpa >= 3.5:
    #if grade == 10 or grade == 11:
    print("DOE OK!")

if (gender.lower() == "f"):
    print("Soccer team OK")

#output
