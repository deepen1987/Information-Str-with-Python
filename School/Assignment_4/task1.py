# CS521 - A2
# Deependrasingh Shekhawat
# Script for Assign Grades

students = list(map(int, input("Enter Scores in integer: ").split(" ")))

for i in range(len(students)):
    if students[i] >= max(students)-10:
        print(f"Student {i} score is {students[i]} and grade is A")
    elif students[i] >= max(students)-20:
        print(f"Student {i} score is {students[i]} and grade is B")
    elif students[i] >= max(students)-30:
        print(f"Student {i} score is {students[i]} and grade is C")
    elif students[i] >= max(students)-40:
        print(f"Student {i} score is {students[i]} and grade is D")
    else:
        print(f"Student {i} score is {students[i]} and grade is F")
