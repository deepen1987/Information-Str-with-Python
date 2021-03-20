n = int(input())

phonebook = {}
for i in range(n):
    key, value = input().split(" ")
    phonebook[key] = int(value)

while True:
    try:
        checkKey = input()
        print(f"{checkKey}={phonebook[checkKey]}" if checkKey in phonebook else "Not found")
    except EOFError:
        break
