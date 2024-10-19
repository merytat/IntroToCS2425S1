math_grade = int(input("Enter your math grade: "))
physics_grade = int(input("Enter your physics grade: "))
literature_grade = int(input("Enter your literature grade: "))

average = (math_grade + physics_grade + literature_grade) / 3

print("Math", math_grade, sep=': ')
print("Physics: ", physics_grade)
print("Literature", literature_grade, sep=': ')
print("Average: ", round(average, 2))

movie = input("Enter your fav movie")
print(movie)