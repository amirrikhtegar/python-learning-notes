# if and else in python 

mark = int(input("----: "))

if mark > 10:
    print(mark)
else:
    print("madod")
# رتبه بندی نمرات

mark = float(input("-----: "))

if mark <= 20 and mark >= 15:
    print("A")
elif mark < 15 and mark >= 10:
    print("B")
elif 10 > mark <= 5:
    print("C")
elif 5 > mark <= 0:
    print("D")
else:
    print("!!!not 0 or 20")    

# جلسه دوم

#  برای این که بتونم دوتا شرط بنویسم که همشه دوتاش برسی بشه باید از یک if جدید استفاده کرد

x = int(input("00000: "))

if x == 5:
    print("amir")
elif x >= 5:
    print(True)

if x <= 5:
    print("دیدی اجرا شد")
    if x == 4:
        print("dorasta")
    elif x == 5:
        print("in dorasta")
    else:
        print("کلا اشتباه")

# نوشتن دیستورات در یک خط 

x = int(input("enter: "))
y = 2 ** x if x >= 4 else 3
print(y)

# مثال

# k2 or k2+1
x = int(input("x :"))

if x % 2 == 0:
    print("k2")
else:
    print("k2+1")

# -----------------

x = int(input("_____: "))
y = int(input("_____: "))
z = int(input("_____: "))
# برای ۲ متغییر
if x < y:
    print("min is x!")
else:
    print("min is y!")
# برای ۳ متغییر
Min = x

if y < Min:
    Min = y
if z < Min:
    Min = z

print(Min)

# تمرین

x = 20

# 1 ------------
if x % 2 == 0:
    print("yes!")
else:
    print("no!")
if x % 5 == 0:
    print("yes!")
else:
    print("no!")
    
if x % 2 == 0 and x % 5 == 0:
    print("Yes!!")
else:
    print("No!!!")    

# 2 ------------
x = 4
y = 3
z = 5

if x < y + z and y < x + z and z < y +x:
    print("ay")
    if x == y and y == z:
        print("df")
    if x == y or y == z or x == z:
        print("ef")
    if x != y and y != z and x != z:
        print("af")
    if x ** 2 == y ** 2 + z ** 2 or y ** 2 == z ** 2 + x ** 2 or z ** 2 == x ** 2 + y ** 2:
        print("\t ayyy")
else:
    print(False)

# 3 ------------

x = "aaaa"

if type(x) == str:
    print("true is string")
elif type(x) == int or float:
    print("true is int")
else:
    print("sayar")

if 48 >= ord(x) >= 57:
    print("adfg")
elif 65 <= ord (x) <= 90 or 97 <= ord(x) <= 122:
    print("this a letter") 
else:
    print("other")

# min , max , sum

l = list(input("''': "))

print(min(x, y, z))
print(min([], default=45))
print(max("amir", "abbse", "babyu"))
print(sum([1, 2, 3, 4, 5], start=24))


