# decorator

# توابع تو در تو 
# ارسال تابع به عنوان ارگومان

def dec(func, f2):
    def inner():
        print("*"*40)
        func()
        f2()
        print("*"*40)
    return inner
    
#@dec# روش اسان برای تبدیل یه دکوراتور
def func(x, y):
    print(x**y)

#@dec
def f2():
    print("ali")

#new_func = dec(func, f2) روش سخت

#new_func()

func(12, 2)

#---------------

def decor(fu):
    def inner(x, y):
        if y != 0:
            print("*"*40)
            fu(x, y)
            print("*"*40)
        else:
            print("warning!!!!!!")
    return inner

@decor
def f(x, y):
    print(x**y)


f(10, 2)


"""
--------------2-------------
"""

def de(fu):
    def inner(*x, **y):
        if y == 0:
            return "rr"
        return fu(*x, **y)
    return inner


@de
def f(x, y, z):
    return x ** y * z

print(f(5, 0, [3]))

print("&"*50)
# ----------------

def plus(func):
    def inner(*x, **y):
        print("+"* 34)
        func(*x, **y)    
        print("+"* 34)
    return inner

def star(func):
    def inner(*x, **y):
        print("*"* 34)
        func(*x, **y)    
        print("*"* 34)
    return inner

@plus
@star
def msg(name):
    print("i am " + name)


printer = plus(star(msg))

printer("attila")

msg("attila")

#----------------------
print("&"*50)

def star(a):
    def inner1(func):
        def inner2(*x, **y):
            print("*" * a)
            func(*x, **y)
            print("*" * a)
        return inner2
    return inner1


@star(int(input("**")))
def mn(name):
    print("I am " + name)


mn("amir")

print("&"*50)
#--------------------------

from functools import wraps

def star(func):
    @wraps(func)
    def inner(*x, **y):
        """ddd inner"""
        print("*"* 34)
        func(*x, **y)    
        print("*"* 34)
    return inner


@star
def msg(name):
    """prints a massage"""
    print("i am " + name)

print(msg.__doc__)
print(msg.__name__)


# ساختار کامل decorator

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        """Do something before"""
        value = func(*args, **kwargs)
        """Do something after"""
        return value
    return wrapper_decorator


# ----------------

from functools import wraps

users = {"ali": "1234", "amir": "2345", "nada": "3456"}

black_list = ("ali")

def black_l(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if args[0] in black_list:
            print("this user is blocked")
        else:
            func(*args, **kwargs)
    return inner


@black_l
def print_password(username):
    print(username, ":", users[username])


@black_l
def change_password(username, new_password):
    users[username] = new_password
    print(username, ":", users[username])

print_password("ali")
change_password("ali", "8734")

# --------------------زمان اجرا
# log 

from time import perf_counter

def time_calculation(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print("the run time of", func.__name__, run_time)
        return value
    return wrapper_decorator


@time_calculation
def a(y):
    s = 0
    for i in range(y):
        s += i**2

@time_calculation
def b(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i

a(1000000000)
b(100000)
