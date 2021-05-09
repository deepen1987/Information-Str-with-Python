persons = [{"Name": "Deependrasingh", "Age": 33}, {"Name": "Neha", "Age": 31}]
tup = (1, 2, 3, 4)
lady = [34, 14, 7, 89]

d1 = {"Name": "Deependrasingh", "Age": 33}
# print(list(filter(lambda x: filter(lambda y: y < 32, x.values()), persons)))
print(d1.items())
print(list(filter(lambda x: x, d1.items())))
