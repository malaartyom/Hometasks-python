a = int(input())
b = a
count = 1 if a < 0 else 0
while a != -1 and a != 0:
    if a & 1:
        count += 1
    a = a >> 1
count = 2 if b == -1 else count
print(count)
