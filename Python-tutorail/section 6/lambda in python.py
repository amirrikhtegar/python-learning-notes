# lambda in python

def func(x):
    return x ** 2

# ----

lambda x: (x ** 2)// 23 * 45

a = lambda x: (x ** 2)

print(a(3))

f = lambda x, y: x * 4 + y ** 2
print(f(5, 2))

# map
lis = [1, 2, 3, 4, 5]

map(func, lis)

nums = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, nums))

print(result)

# filter
# فیلتر کردن بر اساس شرط ما 

li = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(filter(lambda x: x % 2 == 0, li))

print(result)

# ----------

def func(x):
    return x >= 0

lig = [1, 2, 3, -3, -4]

print(list(filter(func, lig)))

print(list(filter(lambda x: x >= 0, lig)))


#reduce

from functools import reduce

def hh(x, y):
    return x + y


li = [1, 2, 3, 4, 5]
print(li)
new = reduce(hh, li)
print(new)
new_1 = reduce(lambda x, y: x + y, li)
print(new_1)

# sorted

li = [1, 2, 3, 4, 5]
li_2 = ["adfsdf", "bfsdsgs", "sc", "ffy"]

new_2 = sorted(li_2, key=len)
print(new_2)

new_3 = sorted(li, key=lambda x: x%3, reverse=True)
print(new_3)


# example

# 1----------------------

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l)
x = list(filter(lambda x: x%2 != 0, l))
print(x)
y = list(filter(lambda x: x % 2 == 0, l))
print(y)

# 2---------------------

se = [("sh", 23), ("a", 2)]

se.sort(key=lambda x: x[1])

# ---------------------------3

lst = [{"weight": 20, "coler": "yed"}, {"weight": 50, "coler": "ted"}, {"weight": 50, "coler": "ged"}, {"weight": 50, "coler": "red"}]

lst.sort(key=lambda x: x["coler"])
print(lst)

# 4--------------------------------

l = [1, 2, 3, 4, 5, 32, 7, 8]
print(l)
x = list(filter(lambda x: x%2 != 0, l))
print(x)
y = list(filter(lambda x: x % 2 == 0, l))
print(y)

# 5------------------------------

l = [1, 2, 3, 4, 5, 32, 7, 8]

print(l)

sq = map(lambda x: x**2, l)

print(list(sq))

cq = map(lambda x: x**3, l)

print(list(cq))

# 6------------------------------

s = "mirirrreewe"

d = lambda s: True if s.startswith("a") else False  

print(d(s))

# 7-----------------------------

s = "5.4"

is_num = lambda s: s.replace(".", "", 1).isdigit()
print(is_num(s))

print(is_num("23213.34"))

print(is_num("12a.3"))
