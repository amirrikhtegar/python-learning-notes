# 1

x = 12
y = 36

s = max(x, y)
d = min(x, y)

for i in range(d, s+1):
    print(i, end=",")

print()

# 2


# روش غییر بیهنه و خودم نوشتم 
x = int(input("x: "))
y = int(input("x: "))

lis1 = []
lis2 = []

i = 1
while i <= x:
    if x % i == 0:
        lis1.append(i)
    i += 1

t = 1
while t <= y:
    if y % t == 0:
        lis2.append(t)
    t += 1

print(lis1, lis2)

lis1 = set(lis1)
lis2 = set(lis2)

print(lis2 & lis1)

# روش دو

lis = []

for i in range(1, min(x,y)+1):
    if x % i == 0 and y % i == 0:
        lis.append(i)
print(lis)

# 3

a, b = x, y

while b != 0:
    a, b = b, a % b
    print(a, b)

print(a)

# روش دو

for i in range(min(x,y), 0, -1):
    if x % i == 0 and y % i == 0:
        print(i)

# 4 

x = 6
y = 12
i = 1

while True:
    if (i % x == 0) and (i % y == 0):
        print("LCM", i)
        break
    else:
        i += 1
        continue

# روش دو

del i
ma = max(x, y)
mi = min(x, y)

for i in range(1, mi+1):
    if (ma * i) % mi == 0:
        print(i)
        break
del i
# روش سوم

i = ma

while i & mi != 0:
    i += ma
print(i)

# 5-------------

x = 123
i = 0
while x > 0:
    x //= 10
    i += 1
print(i)

# 6--------

n = 10
i = 1
while i <= n:
    print(" "* (n-i), end="")
    print("*" * i)
    i += 1

# روش دوم

for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*" * i)

# استفاده از حلقه تو در تو 

for i in range(1, n+1):
    for j in range(0, n-1):
        print(" ", end="")
    for z in range(0, i+1):
        print("*", end="")
    print()

# 7----------------

import random

l = ["a", "b", "c", "d", "e", "f", "g", "h", "u"]

for _ in range(len(l)+1):
    if len(l) == 0:
        break
    i = random.choice(l)
    print(i)
    x = input("no or yas: ")
    if x.lower() == "no":
        l.remove(i)
        print("\n")
    else:
        print("this is your choice", i.upper())
        break

#  روش ۲

name = l.copy()

while True:
    if len(name) == 0:
        break
    user = input("fnvj")
    cmp = random.choice(l)
    ans = input(f"is your guess {cmp}? (y/n):  ")
    if "y" in ans.lower:
        print("you hjj")
        break
    name.remove()

