n = int(input())

arr = []
for i in range(n):
    arr.append(tuple(input().split(" ")))

phonebook = dict(map(lambda x: x, arr))

while True:
    try:
        checkKey = input()
        print(f"{checkKey}={phonebook[checkKey]}" if checkKey in phonebook else "Not found")
    except EOFError:
        break
