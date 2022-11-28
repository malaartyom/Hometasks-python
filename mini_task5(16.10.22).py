def specialize(f, *args, **kwargs):
    def f1(*args1, **kwargs1):
        return f(*args, *args1, **kwargs, **kwargs1)

    return f1


def summ(x, y):
    return x + y


plus_one = specialize(summ, y=1)
print(plus_one(10))
just_two = specialize(summ, 1, 1)
print(just_two())