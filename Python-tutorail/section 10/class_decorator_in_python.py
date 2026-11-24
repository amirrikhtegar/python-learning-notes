from star_for_all_pro import A
from functools import wraps, update_wrapper
a = A()

def decorator_func(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        # do something before the function
        func(*args, **kwargs)
        # do something after the function
    return wrapper_func

a.stare_one_line
# ---------------

def class_decorator_func(cls):
    @wraps(cls)
    def wrapper_func(*args, **kwargs):
        a.stare_one_line
        cls(*args, **kwargs)
        a.stare_one_line
    return wrapper_func

@class_decorator_func
class Test:
    """_summary_
    """
    pass


obj = Test()

print(Test.__doc__)
print(Test.__name__)
#print(obj.n)


class ClassDecorator:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self):
        print("*" * 40)
        return self.func()

@ClassDecorator
def myfunc():
    print("amir")

myfunc()


class ClassDecoratorTwo:
    def __init__(self, cls):
        update_wrapper(self, cls)
        self.cls = cls

    def __call__(self):
        print("*" * 40)
        print(self.cls.__name__)
        obj = self.cls()
        return obj


@ClassDecoratorTwo
class A:
    pass

obj = A()

print(obj)