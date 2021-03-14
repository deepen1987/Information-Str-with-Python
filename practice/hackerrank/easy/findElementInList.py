# Find the Runner-Up Score!
import functools

n = int(input())
arr = map(int, input().split())
arr = sorted(arr, reverse=True)
for i in arr:
    if i < arr[0]:
        print(i)
        break

print(arr)
