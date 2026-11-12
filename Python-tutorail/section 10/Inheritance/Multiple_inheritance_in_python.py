
# * mutiple

#? mro و مشکل الماس

#! وراثت چند گانه کم استفاده میشود و بهتر است استفاده نشود

# m_i

class Superclass1:
    def __init__(self, p1):
        self.p1 = p1
        print("*1")

    def A(self):
        print("1", self)

class Superclass2:
    def __init__(self, p2):
        self.p2 = p2
        print("*2")

    def A(self):
        print("2", self)

    def B(self):
        print("2", self) 


class Subclass(Superclass1, Superclass2):
    def __init__(self, p1, p3):
        super().__init__(p1)
        self.p3 = p3

obj1 = Subclass(1, 2)

print(obj1.p1)

print("*"* 35)
# روش دوم برای init ها

class Superclass1:
    def __init__(self, p1):
        self.p1 = p1
        print("*1")

    def A(self):
        print("1", self)

class Superclass2:
    def __init__(self, p2):
        self.p2 = p2
        print("*2")

    def A(self):
        print("2", self)

    def B(self):
        print("2", self) 


class Subclass(Superclass1, Superclass2):
    def __init__(self, p1, p2, p3):
        Superclass1.__init__(self, p1)
        Superclass2.__init__(self, p2)
        self.p3 = p3

obj1 = Subclass(1, 2, 3)

print(obj1.p1)

