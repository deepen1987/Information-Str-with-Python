# CS521 - A2
# Deependrasingh Shekhawat
# Script for student grading

answers = [
    ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
    ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
    ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
    ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']
]
keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']

student = {}
for i in range(len(answers)):
    for j in range(len(keys)):
        if answers[i][j] == keys[j]:
            if student.get(i):
                student[i] = student[i] + 1
            else:
                student[i] = 1

student = {k: v for k, v in sorted(
    student.items(), key=lambda item: item[1])}

for key, value in student.items():
    print(f"Student {key}'s correct count is {value}")
