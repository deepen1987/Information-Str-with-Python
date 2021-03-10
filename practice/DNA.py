dna = input("Input DNA stain")
output = ''
check = True
for i in dna:
    if i == "G":
        output += "C"
        continue
    if i == "C":
        output += "G"
        continue
    if i == "T":
        output += "A"
        continue
    if i == "A":
        output += "U"
        continue
    if i != "G" or i != "C" or i != "T" or i != "A":
        print("Invalid Input")
        check = False
        break
if check:
    print(output)