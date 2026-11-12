# input ==> function(rule) ==> output

# def example

# algorithm binary search

def binary_search(arr, item):
    low = 0 # A
    high = len(arr) -1 # A

    while low <= high: # B
        mid = (low + high) // 2 # C
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 4, 6, 8, 9]

print(binary_search(my_list, 4)) # == > 2
print(binary_search(my_list, 2)) # == > none

# def in python 

def cube(x):
    print("OK")
    x += 1
    return x ** 3
y = int(23)
n = cube(y)
print(n)

def cube_1():
    x = int(23)
    print("OK")
    x += 1
    return x ** 2
print(cube_1(), "*"*40)
print()
# Example for def (function)

# پیدا کردن تعداد تکرار 


def repeat(number, digit):
    """
    for count of digit in number by math
    """
    count = 0
    while number > 0:
        if number % 10 == digit:
            count += 1
        number //= 10
    return count

print(repeat(12343232313412324, 4))

# روش دوم

def repeat_1(number, digit):
    """
    for count of digit in number by transfor string
    """
    return str(number).count(str(digit))

# example 2

# 1! + 2! + 3! + ... + n!

def factor(n):
    f = 1
    
    for i in range(1, n+1):
        f *= i
    
    return f

def sum_fact(n):
    sum_1 = 0
    
    for i in range(1, n+1):
        sum_1 += factor(i)
    
    return sum_1


number = int(5) # or input
print("sum: ", sum_fact(number))

# example 3

# max or min finder

def max_num(x, y ,z):
    return max(x, y, z)

# argument

#print(max_num(b=2, a=45, c=1))

#print(max_num(12, 10, c=23))

#print(max_num(*[1, 2, 3, 4, 5, 6, 7]))

#*iterable

#max_num(**{"a": 5, "b": 3, "c": 30})


# prametr 

def a_0(n, b, c):# normal
    return n + b + c


def a_1(a=5, b=2):# default value
    return a + b

def a_2(a, b, c=4):# normal + default
    return a + b + c

def a_3(*name):# stare(*)name
    return name

def a_4(a, b, *c):
    return a + b + c

def a_5(**d): # dictionere (**)name
    return d


print(a_5(a=1, b=2, c=4))

def sintask(a, b=1, *c, **d):
    return a, b, c, d

# pointer prametr

def func_12(a, *, b, c):
    return a, b, c 


func_12(1, b=3, c=23)

def func_22(a, b, /, c):
    return a, b, c 

func_22(1, 2, c=10)

# docstring

def Plural(a, b):
    """
    docstrin for sum data 
    """
    return "Plural data", a + b 

print(Plural(12, 23))


print(len.__doc__)
print(max.__doc__)
print(reversed.__doc__)

# function annotition

def func(a:int, b:int, c:int) -> int:
    return "a", a, "b", b, "c", c

print(func(123, 345, "567"))

# __annotations__
print(func.__annotations__)

# mypy

# pip install mypy
# mypy myfile.py
# :int and -> int or strin or ...

print("*"*34, "\n")
# first class function

def func(x:int) -> int:
    print(x*2)

y = func

print("*"*34, "\n")

x = 11
if x > 10:
    def fun(a):
        print(a**2)

fun(6)

print("*"*34, "\n")

def A(a):
    print(a)
    def B(b):
        print(b**2)
    B(a)

A(5)

print(A.__name__)
# print(B.__name__) -- وجود ندارد


def descenfing(li):
    print(sorted(li))

def aesc(li):
    print(sorted(li, reverse=True))

def mysort(f, li):
    f(li)

mysort(aesc, [12, 2, 45, 4, 5, 6])


def my_sort(s):
    
    def descenfing(li):
        print(sorted(li))

    def aesc(li):
        print(sorted(li, reverse=True))

    if s == "a":
        return aesc
    
    elif s == "d":
        return descenfing
    
    else:
        "exit"

s = input("action:a or d ")
fu = my_sort(s)
fu([12, 2, 45, 4, 5, 6])

# Sorting code example

def find_smallest(arr):
    
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index

# exmaple is book algoritm 
print("*"* 60)


# Namespace and scope

# built-in > global > enclosed > local

# built-in
sr = "strin"
print(dir(__builtins__))
print(len(sr))

# global
# محلی هست و مربوط به همون پروژه
x = 1
y = 1
# "x" -> 1
# {"x": 1}
print(globals()) # برای دیدن نام های ما 

globals()["y"] = 10
print(y)

# local 

def a():
    x = 10
    return x

def b():
    print(locals())
    x = 9
    return x

print(a())
print(b())

print(locals())

# encloesing

def a():
    x = 10
    def a_2():
        y = 2

# print(help(locals()))

import math

print("*"*40)

print(math.pi)

print("*"*40)

print(dir(math))

# scope

# built in 

x = 0
if x >= 0:
    y = 10

# local

def A():
    x = 10

# encloesed

def A():
    x = 3
    def B():
        y = 34

# visin local is a scopos

x = 0

def A():
    x = 2
    def B():
        global x
        x += 1
        print(x)
    B()

A()
print(x)


def A():
    x = 2
    def B():
        nonlocal x
        x += 1
        print(x)
    B()



def D():
    x = 11
    def a():
        nonlocal x
        def n():
            nonlocal x
            x += 1
            print(x)
        n()
    a()


D()


# Send by value and send by reference


# pass by value

import copy

def new_func1(func):
    def func(a):
        a += 1
        print(a)

    x = 1
    func(x)
    print(x)
    return func

func = new_func1(func)


def func(a):
    a[1][1] = 12
    print(a)

def new_func(func):
    a = [1, [2, 3, 4], 3, 4 , [2, 3, 4]]
    func(copy.deepcopy(a))
    print(a)

new_func(func)


# example
print("*"*50)
import string
# 1-----------------------------

def len_1(it):
    i = 0 
    for _ in it:
        i += 1
    return i

print(len_1("ASDFGHJKL"))

# 2---------------------

# max()
def max_1(*args):
    m = float("-inf")
    for i in args:
        if m < i:
            m = i
    return m 

print(max_1(12329342943, 34832429, 493824093284, 493280923808, 49238))
        
# 3-----------------------   

# sum()
def sume(*lis):
    s = 0
    for i in lis:
        s += i
    return s

print(sume(12, 213, 3123 , 13213 ,3213))

# 4----------------------

def square(n):
    
    for i in range(1, n):
        
        if i ** 2 == n:
            print(i)
            break
    else:
        print("no!")

n = int(input("n:  "))
print(square(n))

# 5----------------

def tak(a:int, b:int) -> int:
    if b <= 100:
        y = a / 100
        x = y * b
        return int(x)
    else:
        print("no")

print(tak(10000, 50))

# 6----------------------

x = string.ascii_uppercase
y = string.ascii_lowercase
di = string.digits

def lan(a):
    for i in x:
        if i == x:
            print("upper")
    for l in y:
        if l == y:
            print("lower")
    for d in di:
        if d == di:
            print("string")
    

print(lan("2"))

# -------

def func(ch):
    if 48 <= ord(ch) <= 57:
        print("your character is a number")
    elif 65 <= ord(ch) <= 90:
        print("your character is a lowercase letter")
    else:
        print("otherr")

print((func("2")))

# صفات تابع

def func_32(x=0):
    """doc..."""
    pass

print(dir(func))

# درست کردن صفت برای اسم مدرسه های هر تابع

def ave1(li):
    return (sum(li)//len(li))


def ave2(li):
    return sum(li)//len(li)

ave1.school_name = "azade"
ave2.school_name = "freedom"

print(ave1.school_name)

# --------------- متود setattr

def ave(li):
    return (sum(li)//len(li))

setattr(ave, "school_name", "lovers")

print(ave.__dict__)

setattr(ave, "count", 0)

print(getattr(ave, "school_name"))
print(hasattr(ave, "count"))
delattr(ave, "school_name")
# del ave.school_name
