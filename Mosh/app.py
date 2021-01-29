# Code for full triangle
# i = 1
# j = 4
#
# if i == 1:
#   print(' ' * (j + 1) + '*')
# while i <= 5 and j >= 0:
#     print(' ' * j + '*' * i + '*' * (i + 1))
#     i = i + 1
#     j = j - 1
# print('Done')

# Guess Game
# guess_count = 0
# guess_limit = 3
# secret_number = 9
#
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You Won')
#         break
# else:
#     print('You Lost')


# Car Game
# start_count = 0
# stop_count = 0
#
# while True:
#     command = input('>').lower()
#     if command == 'help':
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == 'start':
#         if start_count == 0:
#             print('Car Started...Ready to Go')
#             start_count = 1
#             stop_count = 0
#         else:
#             print('Car is already on are you drunk')
#     elif command == 'stop':
#         if stop_count == 0:
#             print('Car Stopped')
#             stop_count = 1
#             start_count = 0
#         else:
#             print('Car is stopped you idiot drunkard')
#     elif command == 'quit':
#         break
#     else:
#         print("Sorry, I don't understand")


# For Loop
#
# total = 0
# prices = [10, 20, 30]
#
# for item in prices:
#     total = total + item
# print(total)


# Nested loops
#
# numbers = [2, 2, 2, 2, 7]
# for x in numbers:
#     output = ''
#     for y in range(x):
#         output += 'x'
#     print(output)

# List
# number_list = [4, 8, 1, 9, 3]
# largest_number = 0
#
# for find in number_list:
#     if largest_number < find:
#         largest_number = find
# print(largest_number)
#
# print(max(number_list))

# remove duplicate
#
# number_list = [4, 5, 8, 9, 9, 8, 4, 2]
# found = []
#
# for find in number_list:
#     if find not in found:
#         found.append(find)
# print(found)

#  2D Lists
# numbers = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in numbers:
#     matrix = ''
#     for item in row:
#         matrix += str(item)
#     print(matrix)

# Tuple are immutable and can be used in program as immutable containers
# Containers - Tuple, String, List, Dictionary

# Dictionary
#
# libraries = {
#     "name": "Deep singh",
#     "age": 33,
#     "sex": "Male"
# }
#
# print(libraries["age"])

# Using dictionary and its methods
# libraries = {
#     1: "One ",
#     2: "Two ",
#     3: "Three ",
#     4: "Four "
# }
#
# phone = input('Phone: ')
# phone_list = []
# output = ''
#
# for num in range(len(phone)):
#     phone_input = int(phone[num])
#     print(libraries.get(phone_input, "!"), end=" ")

# Smiley converter
# message = input('>')
# words = message.split(' ')
# emoji = {
#     ':)': '😊😊😊',
#     ':(': '😒😒😒'
# }
#
# output = ''
# for word in words:
#     output += emoji.get(word, word) + ' '
# print(output)

# Function
# Parameter(are used when define a function) and
# argument(used when passing a value to function) are different things.
# By default all function in python returns none
# Positional argument and Keyword argument

