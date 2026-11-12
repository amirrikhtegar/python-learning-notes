
# * modules 
from math import *
# ? چرا نباید چیز رو با هم import کنیم؟
# 1. ندیدن ورودی ماژول
# 2. تداخل اسم ها 
# 3. کاهش خوانایی


#! ------------------------
# نحوه import class

# روش اول

from parent.child_1.modul1 import MONTH, Test

print(MONTH)

# 2

from parent import Test

ch1 = Test()
ch1.t("amir")

print(ch1.name)


# پارت ۲ 

# در کلاس باید کلاس های مرطبت کنار هم باشن 
# نباید داخل یک ماژول چند کلاس غیر مرتبت باشد

# روش اول import مستقیم کلاس
from parent.test import Point

# روش دوم ساخت ابجکت و ایمپورت آن

from parent.test import get_obj


p1 = get_obj()
p2 = get_obj()
print(p1)

def func():
    class P():
        pass
    print(P)


func()