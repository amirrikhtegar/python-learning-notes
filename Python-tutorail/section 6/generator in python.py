# کمک به بهینه کردن کد 
# itarator شبیه به مولد(generator)

# -----------

i = iter([1, 2, 3, 4])

print(next(i))
print(next(i))
print(next(i))
print(next(i))
#print(next(i)) -> error

#------------------

def func(x):
    return x ** 2

#print(next(func))

def func(y):
    yield y ** 2
    print("x")
    yield y ** 1
    print("ok")
    yield y - 2

x = func(5)
print(next(x))
print(next(x))
print(next(x))

# استفاده بهتر

def fu():
    print("welcome")
    for i in range(5):
        yield i ** 2


g = fu()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#print(next(g)) - > error stop itaration


# part 2

from time import perf_counter
from functools import wraps

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

# درست کردن range با تابع عادی و ژنراتور

r = range(1, 20, 2)
print(list(r))

# - -- - - -- - - - - -

@time_calculation
def list_range(start, stop, stap=1):
    new_range = []
    
    while start < stop:
        new_range.append(start)
        start += stap
    return new_range


print(list_range(1, 20, 2))

# روش ۲ لاگ گیری


start = perf_counter()

ls = list_range(1, 1000000)

s = 0

for i in ls:
    if i == 10:
        break
    s += i** 2
end = perf_counter()
print("ls: ", end-start)

# - - - - - -- - - - - - - - -- - - - - 

print("*"* 23)

@time_calculation
def range_generator(start, stop, stap=1):
    while start < stop:
        yield start
        start += stap
    
print(list(range_generator(1, 20, 2)))  

# روش ۲ لاگ گیری

start2 = perf_counter()

gr = range_generator(1, 100000000000000000000000000)  

s = 0
for j in gr:
    if j == 10:
        break
    s += j ** 2

end2 = perf_counter()
print("gr: ", end2-start2)

# روش به کارگیری generator

def my_generator(r=10):
    for i in range(r):
        yield i ** 2


g = my_generator()
print(max(g))


#g.throw() # باعث رخ دادن استسنا

#g.send() #

#g.close() # پایان دادن به generator

# yield  تودر تو

def squr(n):
    for i in n:
        yield i ** 2

def even(n):
    for i in n:
        if i % 2 == 0:
            yield i


sq = squr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
eg = even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(sum(squr(even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))))

print("*"* 30)

# example

# example one: enumerate

def custom_enumerate(itarable, start=0):
    conter = start

    for item in itarable:
        yield conter, item
        conter += 1


my_list = ["apple", "banana", "orang", "pianapple"]

print(list(custom_enumerate(my_list, 1)))

# روش اصلی =>

for i in enumerate(my_list, 1):
    print(i)

# example two fibonacci number 

def fibonacci_generator(limit=None):
    a, b = 0, 1
    count = 0
    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1


print(list(fibonacci_generator(limit=23)))

# example tree 

def p_l(itarable):
    count = 0
    for i in itarable:
        h = count + i
        yield h
        count = h


me_list = [1, 2, 3, 4, 5]
print(list(p_l(me_list)))

# example four

s = "amir"

def string_generator(sr):
    x = reversed(sr)
    for i in x:
        yield i


print(list(string_generator(s)))

# روش دیگه 

def reversed_strin_generator(input_string):
    current_index = len(input_string)-1
    
    while current_index >= 0:
        yield input_string[current_index]
        current_index -= 1


print(tuple(reversed_strin_generator(s)))

# example five

def even_number():
    count = 0
    while True:
        yield count
        count += 2
        if count == 100:
            break


print(list(even_number()))

for i in even_number():
    print(i)


def my_gen(even_or_odd="e"):
    count = 0
    if even_or_odd == "o":
        c = 1
    while True:
        yield c
        if c >= 100:
            break
        else:
            c += 2

            
eo = my_gen("o")

for i in eo:
    print(i)

# example six

def func():
    count = 1
    while True:
        s = ""
        for i in range(1, count+1):
            s += f"{count}\t"
            yield s
            count += 1

n = func()
for j in range(10):
    print(next(n))


# list comprehension(Eager)

squares_list = [x**2 for x in range(5)]

print(f"list (Eager): {squares_list}") # [0, 1, 2, 3]

# generator expression (lazy)

squares_gen = (x**2 for x in range(5))

print(f"generator (lazy): {list(squares_gen)}")