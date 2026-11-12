# تابع بازگشتی پر کاربرد نیست 
# برای نوشتن الگوریتم خوب هست 

# recursive func

# سختی ان به این است که برای هر مسئله متفاوت برای حل


def recursive():
    """..."""
    stop_condition = 1
    if stop_condition > 0:
        stop_condition -= 1
        return stop_condition
    recursive()


# شکل کلی تابع بازگشتی

# فاکتوریل با تابع بازگشتی

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!

def fact(x):
    """
    normal function
    """
    f = 1
    for i in range(1, x+1):
        f *= i
    return f

print(fact.__doc__, end="")
print(fact(5))

def fact_recu(x):
    """
    Recursive function
    """
    if x == 0 or x == 1:
        return 1
    return x * fact_recu(x-1)

print(fact_recu.__doc__, end="")
print(fact_recu(5))


def fact_in_book(x):
    """
    Recursive function
    """
    if x == 1:
        return 1
    else:
        return x * fact_in_book(x-1)
    
# example recursive func

from time import sleep 

def func_recur(n):
    """ timer """
    if n <= 0 :
        return print("END")
    sleep(0.05)
    print(n)
    n -= 1
    func_recur(n)

func_recur(10)

# 2

def mul(n):
    
    if n == 0:
        return 1
    elif n % 10 < 5:
        return mul(n // 10)
    else:
        return n % 10 * mul(n // 10)
    

print(mul(1234567))

# 3 

#گرفتن عداد و چاپ کرد مضارب کوچک تر از آن

def func(n):
    if n < 3:
        return
    elif n % 3 == 0:
        print(n)
    func(n-1)

func(10)

# 4 febonach

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))

# point

import functools
from time import sleep

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        """Do something before"""
        print("*" * 40)
        value = func(*args, **kwargs)
        print("#" * 40)
        """Do something after"""
        return value
    return wrapper_decorator


# 1

@decorator
def func_recur(n):
    """ timer """
    if n <= 0 :
        return print("END")
    sleep(0.05)
    print(n)
    n -= 1
    func_recur(n)

func_recur(10)


# 2

def g_rev(n):
    if n <= 0:
        return
    sleep(0.5)
    yield n
    for i in g_rev(n-1):
        yield i


g = g_rev(10)
print(list(g))

print("*" * 10)

# 3
import sys
print(sys.getrecursionlimit)
print("*" * 10)

def func_recur(n):
    """ timer """
    if n <= 0 :
        return print("END")
    sleep(0.05)
    print(n)
    n -= 1
    func_recur(n)

func_recur(10)

# memoization

def memoization(func):
    memo = {}
    @functools.wraps(func)
    def wrapper_decorator(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return wrapper_decorator


@memoization
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(200))

