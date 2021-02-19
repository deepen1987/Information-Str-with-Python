name = ""
score = 0

quit1 = False
stud_dict = {}

while not quit1:
    x = input("Please enter student name and their score ")
    y = input("Please enter student name and their score ")
    stud_dict[x] = y
    if input("Do you want to add more students if yes press 'Y' else 'N': ").upper() == "Y":
        continue
    else:
        quit1 = True

stud_dict = sorted(stud_dict.items(), key=lambda key: key[1], reverse=True)

topper = stud_dict[0]

print(f"Top scorer is {topper[0]} with score {topper[1]}")
