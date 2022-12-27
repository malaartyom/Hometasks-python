class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step

class Singleton:
    flag = False
    instance = None
    def __new__(cls, *args, **kwargs):
        if Singleton.flag:
                cls.__init__ = lambda x: None
        if not Singleton.instance:
            Singleton.instance = object.__new__(cls, *args, **kwargs)
            Singleton.flag = True
        return Singleton.instance 

class GlobalCounter(Singleton, Counter):
    pass

c1 = GlobalCounter()
c1.increment()
c1.increment()
print(c1.count)
c2 = GlobalCounter()
print(c2.count)
print(c1.count)
print(id(c1) == id(c2))