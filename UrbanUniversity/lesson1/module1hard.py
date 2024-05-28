# Grades in alphabetical order
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# Students in random order
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# We use dict comprehension to create a dict
# Keys on the dict are student names from students_set which we have sorted before zipping it with grades list
# Values are student grades
# To calculate average grade we divide the sum of the grades by their number
result = {student: sum(grade)/len(grade) for student, grade in zip(sorted(students), grades)}

print(result)
