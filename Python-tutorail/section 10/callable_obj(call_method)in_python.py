

# ? kwds => kwargs
# * callable object

# 1 obj

def func(x=2):
    return x ** 2

print(func())

# 2 obj

class A:
    def __init__(self, x):
        self.x = x
        print(self.x ** 2)


a = A(2)
print(a.x)
print(callable(func))
print(">" * 3)
# 3 obj

x = 5

# func for chack hav call method or not

def ca(obj, x):
    if callable(obj):
        print("True")
        obj(x)

    else:
        print("this obj not have a call method")


ca(x, 2)
ca(func, 2)
ca(A, 2)
ca(a, 2)

# قابل کال کردن obj ها درکلاس

class B:
    def __init__(self, x):
        print("init")
        self.x = x
    # callable کردن
    def __call__(self, z):
        print("call")
        self.z = 5

ob = B(10)
print(ob.x)

# print(ob.z) 'B' object has no attribute 'z'

# callable کردن
ob(3)
print(ob.z)


# مثال

class Shape:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.area = 0
        self.perimeter = 0


    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def show(self):
        info = ""
        for key, value in self.__dict__.items():
            if value > 0:
                info += f"> {key}: {value:.2f}\n"
        print(info)

    def __str__(self):
        return f"< {type(self).__name__} >"


# self.langth
class Square(Shape):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.langth ** 2

    def calculate_perimeter(self):
        self.perimeter = self.langth * 4

    def __call__(self, langth):
        self.langth = langth


def main():
    s = Square(langth=12)

    s.calculate_area()
    s.calculate_perimeter()
    s.show()

    s(8)
    s.calculate_perimeter()
    s.calculate_area()
    s.show()

if __name__ == "__main__":
    main()
