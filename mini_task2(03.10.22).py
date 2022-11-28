def new_zip(a, b):
    min_len = min(len(a), len(b))
    c = []
    for i in range(min_len):
        c.append((a[i], b[i]))
    return c


a = [1, 2, 3]
b = ["a", "b"]
print(new_zip(a, b))
