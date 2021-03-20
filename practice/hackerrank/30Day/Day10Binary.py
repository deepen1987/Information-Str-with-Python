n = int(input())
count = 0
max1 = 0

while n != 0:
    rem = n % 2
    n = n // 2
    if rem == 1:
        count = count + 1
        if count > max1:
            max1 = count
    else:
        count = 0

print(max1)
