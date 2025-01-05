#input
grades = []
grades.append(int(input("Enter student 1: ")))
grades.append(int(input("Enter student 2: ")))
grades.append(int(input("Enter student 3: ")))
grades.append(int(input("Enter student 4: ")))
grades.append(int(input("Enter student 5: ")))

#process
sum = 0
for cv in grades:
   sum = sum + cv

#output
average = sum / len(grades)
print("Class average: ", average )

counter = 0
for cv in grades:
   if cv > average:
      counter = counter + 1

print("Students above average: ", counter)