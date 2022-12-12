def cycle(itr):
    while True:
        for i in itr:
            yield i

def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break

    return res

print(take(cycle([1,2,3]), 10))