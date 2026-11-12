
# * add method and attr

# pascal case => PascalCase

class Raza:
    pass

# Not snake_case
def snake_case():
    pass


# ساختار کلاس
class Point:
    pass

# ایجاد یک شی از کلاس

p1 = Point() # <__main__.Point object at 0x7fa5bb96d760>
p2 = Point() # <__main__.Point object at 0x7fa5bb96d7c0>

print(p1)
print(p2)
print(id(p1))
print(id(p2))
# این دوشی هیچ رطبی به هم ندارند

def A():
    return "Hi"

x = A()
print(x)
y = A
print(y) # <function A at 0x724692cd3b00>

# اضافه کردن attribute

p1.x = 5.1
p1.y = 3

print("p1.x", p1.x) # 5
print("p1.x", p1.y) # 3

# ! print(p2.x) #error AttributeError: 'Point' object has no attribute 'x'

p2.x = -2
p2.y = -3

# <object>.<attribute> = <value>

# متود و تابع مثل هم هستند به جز داشتن و نداشتن self

# ? تعریف متود در کلاس
print("*"*40)
class PiontB:
    def rest(self):
        print(self)
        self.x = 0
        self.y = 0

pb1 = PiontB()
pb2 = PiontB()

pb1.x = 5
pb1.y = 3
pb1.M = 1

print(pb1.x ,pb1.y)
print(pb1)
pb1.rest()
print(pb1.x ,pb1.y)

# self = باخودت صحبت کن 
# self = یعنی خود ابجکت
# self خودش به صورت خودکار به متود ما در کلاس ارسال میشود 
# pb1.rest(self(automatic))

# روش دوم برای استفاده از متود کلاس ها 

pb1.x = 5
pb1.y = 3
PiontB.rest(pb1)
# ارسال مستقیم شی به متود کلاس

#! بعد از ارسال به method rest
# class PiontB:
#     def rest(pb1):
#         print(pb1)
#         pb1.x = 0
#         pb1.y = 0

# ? مثال دیگر 

from math import hypot

class PointA:
    def move(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        print(self)
        self.move(0, 0)

    def distance(self, other:"PointA") -> float:
        return hypot(self.x - other.x, self.y - other.y)


# how use hypot 
# ? hypot(x1 - x2, y1 - y2)
print(hypot(3, 4)) # 5.0
print("*"* 40)
# ار فرمول فاصله خط استفاده میکند

# نحوه استفاده از کلاس
po1 = PointA()
po2 = PointA()

po1.reset()
print(po1.x, po1.y)

po2.x, po2.y = 8, 4

print(round(po2.distance(po1), 2))

#! ---------------------------------------------------------------------------------------------------
# * init
# مقادر دهی اولیه
from math import hypot

class Point:
    # method
    # attribute -> default / non default
    def __init__(self, x:float=0, y:float=0) -> None:
        #self.x = x
        #self.y = y
        self.move(x,y)
        # نباید retern داشته باشد
    def move(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        print(self)
        self.move(0, 0)

    def distance(self, other:"Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)

ob_p1 = Point(3, 4)
ob_p2 = Point(0, 0)
ob_p3 = Point()
print(ob_p3)

print(ob_p1.distance(ob_p2))
print(ob_p3.distance(ob_p1))
#print(ob_p.x) attr Error 


# __new__ -> create object
# __init__ -> initialize attr

#! ---------------------------------------------------------------------------------------------

