fullGrade = int(input("Enter the total for CA - CD: "))
grade = 0

if fullGrade >= 28:
    grade = 7
elif fullGrade >= 23:
    grade = 6
elif fullGrade >= 19:
    grade = 5
elif fullGrade >=15:
    grade = 4
elif fullGrade >= 10:
    grade = 3
elif fullGrade >= 6:
    grade = 2
elif fullGrade >= 1:
    grade = 1
else:
    grade = 0

print("MYP Grade: ", grade)
