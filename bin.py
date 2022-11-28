a = {1: 17, 2: 15, 3:9, 4:21}
print(min(a, key = lambda x: a[x]))
if (1, 17) in a.items():
    print(1)
else:
    print(0)