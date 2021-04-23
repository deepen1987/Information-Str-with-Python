p = [("label1", ["I", "deep", "neha", "so", "harvard"])]

print(list(map(lambda x: list(filter(lambda x: len(x) > 2, x[1])), p)))
