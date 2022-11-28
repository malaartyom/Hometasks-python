import functools


def deprecated(f=None, since=None, will_be_removed=None):
    if f is None:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)
    def inner(*args, **kwargs):
        first = f"Warning: function {f.__name__} is deprecated"
        second = "."
        third = " It will be removed in"
        fourth = " future versions "
        if since is not None:
            second = f" since version {since}."
        if will_be_removed is not None:
            fourth = f" version {will_be_removed}"
        print(first + second + third + fourth)
        f(*args, **kwargs)


    return inner

@deprecated(since="4.2.0", will_be_removed="5.0.1")
def foo():
    print("Hello from foo")
@deprecated
def bar():
    print("Hello from bar")
@deprecated(will_be_removed="5.0.1")
def buz():
    print("Hello from buzz")

foo()
bar()
buz()
