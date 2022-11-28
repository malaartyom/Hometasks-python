def flatten(a):
    ret_a = []
    for i in a:
        if isinstance(i, list):
            ret_a.extend(flatten(i))
        else:
            ret_a.append(i)
    return ret_a

a = [1, 2, [4, 5], [6, [7]], 8, [9,[10,[11,12,13,[14,15,[16,17,[18,19]]]]]]]
print(flatten(a))