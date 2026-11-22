lazy from star_for_all_pro import A
a = A()

class Myclass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


c = Myclass(1, 2)

print(c.__dict__)

c.c = 3

print(c.__dict__)

a.stare_one_line
# اضافه کردن attr با 
c.__dict__["d"] = 4

print(c.__dict__)

a.stare_twe_line

class Myclass:
    # for manegmant my attribute
    __slots__ = ("a", "b", "d")
    
    def __init__(self, a, b):
        self.a = a
        self.b = b


d = Myclass(1, 2)

print(d.a)

#d.c = 3 'Myclass' object has no attribute 'c' and no __dict__ for setting new attributes

d.d = 3 # not error

a.stare_twe_line

class ParentClass:
    __slots__ = ("a", "b") 
    
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ChildClass(ParentClass):
    __slots__ = ("c") 

    def __init__(self, a, b):
        super().__init__(a, b)

obj = ChildClass(1, 2)
#print(obj.__dict__)
obj.c = 3
#print(obj.__dict__)
print(obj.c)