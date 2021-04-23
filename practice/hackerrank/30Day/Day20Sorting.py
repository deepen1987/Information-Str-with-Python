#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numberOfSwaps = 0
for i in range(n):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1

print(f"""Array is sorted in {numberOfSwaps} swaps.
First Element: {a[0]}
Last Element: {a[-1]}""")
