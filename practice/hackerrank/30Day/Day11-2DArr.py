def hour_glass(x, y):
    ret_array = []
    for a in range(x, x + 3):
        for b in range(y, y + 3):
            ret_array.append(input_array[a][b])
    return ret_array


def compute_array(d):
    total = 0
    for k in range(len(d)):
        if k != 3 and k != 5:
            total = total + d[k]
    return total


input_array = []
for i in range(6):
    input_array.append(list(map(int, input().rstrip().split())))

output_array = []
for i in range(4):
    for j in range(4):
        output_array.append(hour_glass(i, j))

max_total = -2147483648
max_array = []
for c in output_array:
    total = compute_array(c)
    if total > max_total:
        max_array = c
        max_total = total

print(max_total)
