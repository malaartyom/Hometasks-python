def chain(*args):
    for i in args:
        yield from i

my_list = [42, 13, 7]
print(list(chain([1,2,3], ['a', 'b'], my_list)))