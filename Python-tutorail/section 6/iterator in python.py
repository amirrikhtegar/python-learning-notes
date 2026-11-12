# iterate -> تکرار کردن 

# iteration -> تکرار
# for , while

# iterable -> تکرار پذیر

x = [1, 2, 4, 6]

for i in x:
    s = i ** 2
    print(s)

# ------------

print("__iter__" in dir(x))
print("__iter__" in dir((1 ,2, 3, 4))) 
print("__iter__" in dir(True)) # bool

# ------------------
print("*"*23)


i = [1, 2, 3, 4]

print("__next__" in dir(i))
print("__iter__" in dir(i))

i = iter(i)
print("__next__" in dir(i))

print("*"*23)

print(next(i))
print(next(i))
print(next(i))
print(i.__next__())

i = iter(i)

while True:
    try:
        print(next(i))
    except StopIteration:
        break

for l in i:
    print(i)

from itertools import count
print(dir(count))
counter = count(10)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

a = [1, 2, 3]

print(hasattr(a, "__iter__"))

