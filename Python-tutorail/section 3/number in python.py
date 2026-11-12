# numbers in Python
# integers, float and complex numbers

a = 10          # int
b = 3.14        # float
c = 2 + 3j     # complex

print(bin(a))        # Output: 0b1010
print(hex(a))        # Output: 0xa
print(oct(a))        # Output: 0o12

print(int(b))       # Output: 3
print(float(a))     # Output: 10.0
print(complex(a))   # Output: (10+0j)

x = 0b1010
y = 0o12
z = 0xa

print(x, y, z)      # Output: 10 10 10

print(type(a))      # Output: <class 'int'>
print(type(b))      # Output: <class 'float'>
print(type(c))      # Output: <class 'complex'>

cv = float(a)
print(type(cv))     # Output: <class 'float'>
iv = int(b)
print(type(iv))     # Output: <class 'int'>
cc = complex(a)
print(type(cc))     # Output: <class 'complex'>

from decimal import Decimal
print(type(float(Decimal("0.6") + Decimal("0.3"))))
print(0.6 + 0.3)

import fractions
print(fractions.Fraction(2.1))

print(1_000_000)
print(1e6)
print(100e500+200) # infinity

bn = 10 + 2j
print(bn.real)  # Output: 10.0
print(bn.imag)   # Output: 2.0

vb = 3.14323459
print(round(vb, 1)) 
print(abs(-10))  # Output: 10
print(pow(2, 3))  # Output: 8

# تبدیل کیلوگرم به گرم

kg = int(input("Enter weight in kg: "))
print(type(kg))
gr = kg * 1000
print("gr = ", gr, "gr", sep="")

# مساحت مثلث برابر با قاعده *ارتفاع تقسیم بر ۲ است

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
area = (base * height) / 2
print("Area of triangle =", area)

# ماشین حساب ساده

x = int(input("enter your x:"))
y = int(input("enter your y:"))
print(x, "+", y, "=", x + y)
print(x, "*", y, "=", x % y)

# جدا کردن اعداد وارد شده توسط کاربر

# هر عددی بر % باعت می شود رقم آخر عدد جواب باشد

print(234 % 10)  # Output: 4
print(234 // 10) # Output: 23

x = int(input("enter numbers for separate:"))

temp = x % 10
print(temp)

x = x // 10
temp = x % 10
print(temp)

x = x // 10
temp = x % 10
print(temp)

# تبدیل درجه به رادیان و بالعکس

x = float(input("enter degree:"))
r = x * 3.14 / 180
print("radian =", r)

# تمرین
# 1
p = 3.14 
r = int(input("enter your degree:")) 
area = 2 * p * r
print(area)
Environment = p * r ** 2
print(Environment)

# 2

x = int(input("enter your number:"))
x_Square = x ** 2
x_Cube = x ** 3
print("square:", x_Square, "cube:", x_Cube, sep="")

# 3

x = int(input(":"))
y = int(input(":"))
z = x ** y
print("tavan", z)

# 4

x = int(input("enter your number:"))
y = int(input("enter your number:"))
z = int(input("enter your number:"))
avrage = (x + y + z) / 3
print("avrage =", avrage)
