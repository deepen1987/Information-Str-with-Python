# CS521 - A2
# Deependrasingh Shekhawat
# Script for counting positive and negative numbers and average of numbers

count = 0
number_of_positive = 0
number_of_negative = 0

while True:
    user_value = int(input("Enter an integer, the input ends if it is 0: "))
    if count == 0 and user_value == 0:
        print("You didn't enter any number")
        break
    if user_value > 0:
        number_of_positive += 1
        count += 1
    if user_value < 0:
        number_of_negative += 1
        count += 1
    if user_value == 0:
        count += 1
        average_value = float(count / (number_of_positive + number_of_negative))
        print(f"""The number of positives is {number_of_positive}
The number of negatives is {number_of_negative}
The total is {count}
The average is {average_value}""")
        break

