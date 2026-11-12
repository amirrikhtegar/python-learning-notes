# module

# ماژول داخل

#1
import random 

l1 = [1, 2, 3, 4, 5]

print(random.choice(l1))

#2

import datetime

print(datetime.date.today())

# حالت دوم قابل نصب

import numpy as np

print(f"آتیلای عزیز، Numpy نسخه {np.__version__} در لینوکسِ دوست‌داشتنیِ تو نصب شد!")

# how to create module

def greet(name):
    return f"سلام {name} عزیز! خوش آمدی به دنیای ماژول‌ها!"

def add(a, b):
    return a + b

name = "amir"

# how to import module

#import pk1.pak.mod1

# privit vareble
name1 = "nada"
_age = 34

# all file is module

print(__name__)

if __name__ == "__main__":
    greet(name)
    add(12, 1)
    print("hello!")



#import test

#print(test.func(2))

# how to inderstan what is local is my module

import sys
sys.path.append("/home/lord/Desktop/test")
for i in sys.path:
    print(i)

import test

#print(func(2))
