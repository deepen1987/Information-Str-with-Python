# for i in range(ord("F"), ord("Q")):
#     print(i)

n = int(input().strip())
if (n % 2) != 0:
    print("Weird")
if n % 2 == 0 and 1 < n < 6:
    print("Not Weird")
if n % 2 == 0 and 5 < n < 21:
    print("Weird")
if n % 2 == 0 and n > 20:
    print("Not Weird")
