# for loop in python 

# تفاوت for , while

List = [1, 2, 3, 4]

i = 0

while i < 4:
    print(List[i])
    i += 1

print("*"* 40)

# مورد استفاده ها در for

List = [1, 2, 3, 4]

Tuple = (1 ,2 ,3 ,4)

String = "amir mohmmad"

dictionere = {"amir":1, "ali":2, "parisa":3}

for i in String:
    print(i)
    
print("*"* 40)

# چاپ کردن کارکتر کد های اسکی

List_1 = [56, 34, 87, 125]

for ASCII in List_1:
    if ASCII <= 100:
        print(chr(ASCII))
    
print("*"* 40)

# جدا کردن عضای مثل هم و متفاوت از هم 

l_1 = [1, 2, 3, 4, 5]
l_2 = [23, 1, 45, 5, 2, 45]

for num in l_1:
    for nam in l_2:
        if num == nam:
            print(num)

print("*"* 40)

# بهینه تر

for num in l_1:
    if num in l_2:
        print(num)

print("*"* 40)

# مثال پیچیده تر

a, *b, c = [1, 2, 3, 4, 5, 6]

print(a, b, c)
print("*"*10)
for a, b, *c in [[1 ,2 ,3], [4, 5, 6, 80], [7, 8, 9]]:
    print(a)
    print("*")
    print(b)
    print("*")
    print(c)
    print("*"*10)


d = {"a": 1, "b": 2, "c": 3}

for k in d.items():
    print(k)

for k, v in d.items():
    print(k, ":", v)

print("8"*20)

# با استفاده از مجموعه

s = {1 ,2 , 3, 4}

for gf in s:
    print(gf)

print("*"*40)

# range metod in for loop

l = input("names: ").split(",")

for i in range(10):
    print(i)

print("*"*40)

for i in range(1, 23, 3):
    print(i)

print("*"*40)

for i in range(-20, -150, -10):
    print(i)

print("*"*40)

for i in range(0, len(l)):
    print(i, l[i])

print("*"*40)

# نوشتن فاکتوریل

n = int(input("n: "))
j = 1 # این متغیر برای ذخیره هست و برای بی تعصیر بودنش مقدار ۱ دارد
for i in range(1, n+1):
    j *= i
    print(i, "ok", j)

print("F!: ", j)

print("*"*40)

print(list(range(1, 4, 2)))

# معکوس کردن عدد

n = input("n: ")

for i in range(len(n)-1, -1, -1):
    print(n[i], end="")
print()
print("*"*10)

# روش دوم 

n = input("'n: '")
s = ""
for i in range(len(n)-1, -1, -1):
    s += n[i]

x = int(s)

print(x)

print("*"*10)

n = int(input("''''n : ;;;;"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print("")

print("*"*10)

for i in range(n-1, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()

print("*"*10)

# enumerate

my_list = ["apple", "banana", "cherry", "blueberi", "orang", ",..."]

print("*"*10)

print(tuple(enumerate(my_list)))

print("*"*10)

for i in range(0, len(my_list)):
    print(i, my_list[i])

print("*"*10)

for index, fruit in enumerate(my_list):
    print(f"Index: {index}, Fruit: {fruit}")

print("*"*10)

for index1, fruit1 in enumerate(my_list, start=2):
    print(f"Index: {index1}, Fruit: {fruit1}")
    
print("*"*10)

names = ["amir", "ali", "attila"]
ages = [25, 30, 18]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

print("*"*10)

for neme2 in reversed(my_list):
    print(neme2)

print("*"*10)

for name2 in sorted(my_list, reverse=True):
    print(name2)

print("*"*10)

# random module

from random import random, seed, uniform, randint, randrange, choice, sample, shuffle 

for i in range(1):
    seed = 10
    print(random())
    print(random())

print("*"*10)

# min + (random * (max - min))

print(5 + (random( ) * (10 - 5)))

print("*"*10)

print(uniform(5, 10))

print("*"*10)

print(randint(5,1525))

print("*"*10)

l = ["a", "b", "c", "d"]

for _ in range(4):
    print(choice(l))

print("*"*10)

for _ in range(4):
    print(randint(l[0, len(l)-1]))# همان کار تابع چویز را انجام میدهد

print(sample(l, 3))

print(randrange(1, 10, 2))

y = l.copy

print(shuffle(y))

# شیر یا خط

l = ["lion", "line"]
x = 0
y = 0

for _ in range(10):
    if random.choice(l) == "lion":
        print("شیر")
        x += 1
    elif random.choice(l) == "line":
        print("خط")
        y += 1

print("lion", x)
print("line", y)
    
# پرتاپ تاس

disc = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for _ in range(1000):
    disc[randint(1, 6)] += 1

print(disc)


