# coroutine in python 

# send at func 

def my_gen():
    print("ready!!")
    while True:
        n = yield 
        print("my name is: ", n)


g = my_gen()

next(g)
next(g)
next(g)
print(g.__next__())
g.send("amir")

# مدل دیگر
print("*"* 34)


def me_gen():
    print("start!")
    for i in range(10):
        new = yield i
        print("my name is:", new)



ge = me_gen()

print(next(ge))
print(g.send("amir"))
print(next(ge))
print(g.send("attila"))

# --------------------------- استفاده از send بدون نوشتن next

from functools import wraps

def coroutine(func):
    @wraps(func)
    def start(*args, **kwargs):
        gn = func()
        next(gn)
        return gn
    return start



@coroutine
def me_ge():
    print("start!")
    for i in range(4):
        new = yield i
        print("my name is:", new)


fg = me_ge()

print(fg.send("amir"))
print(fg.send("asgar"))
print(fg.send("attila"))
# print(fg.send("ali"))

# مثال ها 

# سانسور کلمات

def cen_gen(words):
    print("start")
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = "*" * (len(word)+1)



g = cen_gen(["kos", "cos", "kir"])


next(g)
print(g.send("attila"))
print(g.send("amir"))
print(g.send("ali"))
print(g.send("cos"))
print(g.send("kir"))

# split توسط generator

def spl_gen(delimiter=" "):
    print("start")
    s = None
    while True:
        line = yield s
        s = line.split(delimiter)


df = spl_gen(",")

next(df)

print(df.send("attila,amir,ali,asgar,hasan"))
