class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step

class Singleton:
    class_exists = False
    def __new__(cls, *args, **kwargs):
        if Singleton.class_exists:
            Singleton.class_exists = True
            return object.__new__(cls, *args, **kwargs)
        else:
            return None

class GlobalCounter(Singleton, Counter):
    pass

c1 = GlobalCounter()
c2 = GlobalCounter()
print(id(c1) == id(c2))