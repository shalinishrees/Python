"""Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
Example
The ordered list of scores is , so the second lowest score is . There are two students with that score: .
Ordered alphabetically, the names are printed as:
alpha
beta"""
#without using built-in function
n = int(input())
names = []
grades = []

for i in range(n):
    names.append(input())
    grades.append(float(input()))

lowest = grades[0]
for g in grades:
    if g < lowest:
        lowest = g
second_lowest = None
for g in grades:
    if g > lowest:
        if second_lowest is None or g < second_lowest:
            second_lowest = g

result = []
for i in range(n):
    if grades[i] == second_lowest:
        result.append(names[i])

size = len(result)
for i in range(size):
    for j in range(size - 1 - i):
        if result[j] > result[j + 1]:
            temp = result[j]
            result[j] = result[j + 1]
            result[j + 1] = temp


for name in result:
    print(name)


  #with built-in function 
  n = int(input())
students = []
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])
grades = sorted(set(grade for name, grade in students))
second_lowest = grades[1]
result = sorted(name for name, grade in students if grade == second_lowest)
for name in result:
    print(name)
