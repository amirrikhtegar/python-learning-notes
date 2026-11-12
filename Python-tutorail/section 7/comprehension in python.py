# comprehension 

# example 1
# غییر بهینه
print("normal")

s = []
for i in range(1, 10):
    s.append(i ** 2)
print(s)

# بهینه تر 
print("comprehension")

x = [i ** 2 for i in range(10)]
print(x)

# با map
m = list(map(lambda i : i**2 , range(10)))

print("\n", "*" * 40, "\n")

# example 2

x = [i ** 2 for i in range(10) if i % 2 == 0]

print(x)

# or

x = [i ** 2
     for i in range(10)
        if i % 2 == 0]

print(x)

print("\n", "*" * 40, "\n")

# example 3

s1 = [1, 2, 3]
s2 = [4, 2, 3]
s = []

for i in s1:
    for j in s2:
        if i != j:
            s.append((i, j))

print(s)

# or comprehension

l1 = [1, 2, 3, 4]
l2 = [3, 2, 4, 1]
l_or = [(i, j) for i in l1 for j in l2 if i != j]

print(l_or)

print("\n", "*" * 40, "\n")

# example 4 

z = [-1, -12, -3, 5, 6, 1, 3, -1]
x = [abs(n) for n in z if abs(n) >= 1]
print(x)

print("\n", "*" * 40, "\n")

# example 5

names = ["reza", "amir", "attila"]

x = [ch.upper() + "**" for name in names for ch in name]

print(x)

# or normal

s = []

for name in names:
    for ch in name:
        s.append(ch.upper()+ "**")

print(s)
print("\n", "*" * 40, "\n")

# example 6 by math
from math import pi

s = []

for i in range(10):
    s.append(str(round(pi, i)))

print(s)

# or comprehension

ma = [str(round(pi, i)) for i in range(10)]

print(ma)

print("\n", "*" * 40, "\n")

# example 7 hard

# list comprehension

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

t = []

for i in range(3):
    t_row = []
    for row in matrix:
        t_row.append(row[i])
    t.append(t_row)

print(t)

# or

t1 = [[row[i] for row in matrix] for i in range(3)]

print(t1)

# or تبدیل با zip

t2 = list(zip(*matrix))

print(t2)

print("\n", "*" * 40, "\n")

# ادامه

x = "a"
c = [x for x in (1, 2, 3)]

print(x)

# genrator 

c = (i for i in range(4) if i % 2==0)

print(next(c))
print(next(c))

# -----

t = (1, 2, 3, 4)

c = [i for i in t]

# or 

c = list(t)

# set comprehension

x = "ffjapdkpokfpdskfskf[aakdoefkjvmk]"

s_set = {i for i in x}

s = {i for i in range(10) if i % 2 != 0}

print(s_set)

# for dict
x = {"ali": 24, "nada": 12, "ali": 23}

s = {key : value for key, value in x.items()}

d1 = ["a", "b", "c"]
d2 = [23, 45, 12]
s = {key:value for key, value in zip(d1, d2)}
print(s)

x = [1, 2, 3, 4, 4, 12, 3, 7]

y = []

def func(x):
    if x % 2 == 0:
        return x
    else:
        return "Na"

for i in x:
    y.append(i if i % 2 != 0 else 0)

print(y)

v = [j if j % 2 == 0 else "Na" for j in x]

print(v)

w = [func(j) for j in x]


#   

from random import randrange

def func_1():
    return randrange(50, 150)


x = [n for _ in range(10) if (n := func_1()) > 100]

print(x)

df = []
for _ in range(10):
    if (n := func_1()) > 100:
        df.append(n)

print(df)


# -----------------------

def func_2():
    return randrange(10000, 100000)

names = ["reza", "amir", "attila"]

d = {k:[func_2() for _ in range(len(names))] for k in names}

print(d)

