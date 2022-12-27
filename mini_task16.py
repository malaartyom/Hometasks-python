from random import randint
import numpy as np
import time
start = time.time()
def field_sum(field):
    summ = 0
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j]:
                summ += 1
    return summ
def count_neighbours(a, i, j, size):
    count = 0
    if (i < size - 1) and (j < size - 1):
        if field[i - 1][j]:
            count += 1
        if field[i + 1][j]:
            count += 1
        if field[i][j + 1]:
            count += 1
        if field[i - 1][j + 1]:
            count += 1
        if field[i + 1][j + 1]:
            count += 1
        if field[i][j - 1]:
            count += 1
        if field[i - 1][j - 1]:
            count += 1
        if field[i + 1][j - 1]:
            count += 1
    elif i == size - 1 and j < size - 1:
        if field[i - 1][j]:
            count += 1
        if field[0][j]:
            count += 1
        if field[i][j + 1]:
            count += 1
        if field[i - 1][j + 1]:
            count += 1
        if field[0][j + 1]:
            count += 1
        if field[i][j - 1]:
            count += 1
        if field[i - 1][j - 1]:
            count += 1
        if field[0][j - 1]:
            count += 1
    elif i < size - 1 and j == size - 1:
        if field[i - 1][j]:
            count += 1
        if field[i + 1][j]:
            count += 1
        if field[i][0]:
            count += 1
        if field[i - 1][0]:
            count += 1
        if field[i + 1][0]:
            count += 1
        if field[i][j - 1]:
            count += 1
        if field[i - 1][j - 1]:
            count += 1
        if field[i + 1][j - 1]:
            count += 1
    elif i == size - 1 and j == size - 1:
        if field[i - 1][j]:
            count += 1
        if field[0][j]:
            count += 1
        if field[i][0]:
            count += 1
        if field[i - 1][0]:
            count += 1
        if field[0][0]:
            count += 1
        if field[i][j - 1]:
            count += 1
        if field[i - 1][j - 1]:
            count += 1
        if field[0][j - 1]:
            count += 1        
    return count
def print_field(field):
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j]:
                if j != len(field) - 1:
                    print("1", end=" ")
                else:
                    print("1")
            else:
                if j != len(field) - 1:
                    print("0", end=" ")
                else:
                    print("0")
                
    
size = 128
iterations = 128
field = []
for i in range(size):
    string = []
    for j in range(size):
        string.append(0)
    field.append(string)
field[0][2] = 1
field[1][0] = 1
field[1][2] = 1
field[2][1] = 1
field[2][2] = 1
# print_field(field)
# print()
# print(count_neighbours(field, 1, 2, size))
#while field_sum(field) != 0:
# for i in range(size):
#     for j in range(size):
#         if j == size - 1:
#             print(count_neighbours(field, i, j, size))
#         else:
#             print(count_neighbours(field, i, j, size), end = " ")
# print()
for k in range(iterations):
    for i in range(size):
        for j in range(size):
            if field[i][j] == 0 and count_neighbours(field, i, j, size) == 3:
                field[i][j] = 1
            elif field[i][j] == 1 and (count_neighbours(field, i, j, size) < 2 or count_neighbours(field, i, j, size) > 3):
                field[i][j] = 0
end = time.time()
start1 = time.time()
field1 = np.array([])
for i in range(size * size):
    field1 = np.append(field1, 0)
field1 = field1.reshape(size, size)
field1[0][2] = 1
field1[1][0] = 1
field1[1][2] = 1
field1[2][1] = 1
field1[2][2] = 1
for k in range(iterations):
    for i in range(size):
        for j in range(size):
            if field1[i][j] == 0 and count_neighbours(field1, i, j, size) == 3:
                field1[i][j] = 1
            elif field1[i][j] == 1 and (count_neighbours(field1, i, j, size) < 2 or count_neighbours(field1, i, j, size) > 3):
                field1[i][j] = 0
end1 = time.time()
print(f"Время работы программы с обычными списками: {end - start}")
print(f"Время работы программы с NumPY списками: {end1 - start1}")



