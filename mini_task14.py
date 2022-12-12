import functools

@property
def coroutine(f = None):
    """if f is None:
        return functools.partial(coroutine)"""
    def inner(*args, **kwargs):
        a = f(*args, **kwargs)
        next(a)
        return a
    return inner

@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)

st = storage()
print(st.send(42))
print(st.send(42))