lazy from polymotphism_in_python import Cow
#
# * duck

s = "raza"
l = [1 ,2 ,3 ,4]
t = (1 ,2 ,3 ,4)

print(len(s))
print(dir(s))
print(len(l))
print(dir(s))
print(len(t))
print(dir(t))

# ! evreone have len in dir

# * LBYL -> look before you leap

def check_len(obj):
    if hasattr(obj, "__len__"):
        print(len(obj))

    else:
        print("sorry dude")

i = 3

check_len(i)

# * EAFP -> it's  easir to ask for forgiveness than permission

def check_len_2(obj):
    try:
        print(len(obj))
    except:
        print("sorry...")


check_len_2(i)

d = {"a": 1, "b": 2, "c": 3}

try:
    print(d["a"])
except:
    print("sorry dude")

try:
    print(d["f"])
except:
    print("sorry dude")


# * duck 2

class Duck:
    def move(self):
        return "I'm swimming,,,,"

class Person:
    def move(self):
        return "I'm walk to my home"

class Car:
    def move(self):
        return "I'm driveing"

def func(obj):
    print(obj.move())

d = Duck()
p = Person()
c = Car()

func(d)
func(p)
func(c)


c = Cow()
print(c.make_sound())

