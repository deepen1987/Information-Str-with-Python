items = [("prod3", 12), ("prod1", 9), ("prod2", 14)]
prices = []
for item in items:
    prices.append(item[1])
print(prices)

prices1 = list(map(lambda abc: abc[1], items))
print(prices)

prices2 = list(filter(lambda abc: abc[1] > 10, items))
print(prices2)

# list comprehension

prices3 = [item[1] for item in items]
print(prices3)

i = [1, 2]
j = [3, 4]

k = list(zip("ab", "78", i, j))
print(k)
