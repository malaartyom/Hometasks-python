import functools

def coroutine(f):
    @functools.wraps(f)
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

print(storage.__name__)
print(st.send(42))
print(st.send(42))