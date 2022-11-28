import math
def flatten(a, depth = math.inf):
    ret_a = []
    for i in a:
        if isinstance(i, list) and depth != 0:
            ret_a.extend(flatten(i, depth - 1))
        else:
            ret_a.append(i)

    return ret_a

a = [1, 2, [4, 5], [6, [7]], 8, [9,[10,[11,12,13,[14,15,[16,17,[18,19]]]]]]]
b = [1, 2, [4, 5], [6, [7]], 8,]
print(flatten(a))
print(flatten(b))
print(flatten(b, depth=1))
print(flatten(a, depth=3))
