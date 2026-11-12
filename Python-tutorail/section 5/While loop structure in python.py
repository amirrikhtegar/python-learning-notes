# while loop

# توضییح اول با استفاده از مثال جریمه تکرار معلم

word = 0
while word <= 10  :
    print("hello")
    word += 1

print("-" * 40)

# مثال دوم پیدا کردن اعداد زوج

n = 10

while n < 100 :
    if n % 2 == 0 and n % 7 == 0:
        print(n)
    n += 1

while n < 1000 :
    if n % 3 == 0 and n % 7 == 0 :
        print(n)
    n += 1

# چاپ مثلث

r = 1

while r <= 100 :
    print("*" * r)
    r += 1


# مثلث بر عکس 

n = 12

while n >= 1 :
    print("x" * n)
    n -= 1

print("\n", n)

# مقسوم الیه ها 

# 12 -> 1 , 12 , 3 ,2 ,6
 
x = 6 # 12
i = 1
lis = []
while i <= x :
    if x % i == 0:
        print(i)
        lis.append(i)
    i += 1
print(lis) # [1, 2, 3, 4, 6, 12]

# پیدا کردن عداد کامل

# روش اول
if sum(lis)-x == x:
    print(True)
else:
    print(False)

# روش دوم

c = 0

while i < x :
    if n % i == 0:
        c += i
    i += 1

if c == x:
    print(True)
else:
    print(False)

# مثال سخت تر چاپ فیبوناچی

# 0, 1 , 1, 2, 3, 5, 8, 13, 21, 34, ...

i = 1
a, b = 0, 1
while i <= 20 :
    print(b)
    a, b = b, a + b # باید این جوری نوشته بشه تا همزمان کار کنند
    # a = b
    # b = a+b این روش اشتباه هست
    i += 1

# break , continue , else in while

i = 1
while i <= 100:
    if i == 5:
        break
    print(i)
    i += 1

print("x"* 40)

# مثال برای پیدا کردن کوچک ترین با استفاده از دستورات 
# برای برک
m = float("inf")
print(m + 1)

while True:
    n = float(input("n: "))
    if n < m:
        m = n
    s = input("do you continue?")
    if s.lower() == "no":
        break
else:
    print("ok")

print(m, "is smallest number!")

# برای کانتنیو

i = 0
while i <= 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
else:
    print("ok")

# برای else
# پیدا کردن عداد اول
n = int(input("nh : "))
i = 2
if n > 1:
    while i < (n//2)+ 1:
        if n % i == 0 :
            print(n , "is not prime number!")
            break
        i += 1
    else:
        print(n, "is a prime number!")
else:
    print("no no")

print("x"* 40)

# nested loop
# loop 1
i = 1
while i <= 10:
    # loop 2
    j = 1
    while j <= 10:
        print("\t", j)
        j += 1 # 11
    print(i)
    i += 1

print("x"* 40)

# چاپ کردن عضای لیست

l = ["amir", "ali", "asgar", "parisa"]

i = 0 # چرا از صفر استفاده کردیم چون index های ما از 0 شروع می شود

while i < len(l):
    s = l[i]
    j = 0
    while j < len(s):
        if j % 2 == 0:
            print(s[j].upper(), end="")
        else:
            print(s[j], end="")
        j += 1
    print()
    i += 1

print("x"* 40)


# یکم پیچیده تر

l = ["amir", "ali", "asgar", "parisa"]

i = 0

while i < len(l):
    print(l[i])
    j = 0
    while j < len(l[i]):
        if j % 2 == 0:
            print(l[i][j].upper(), end="")
        else:
            print(l[i][j], end="")
        j += 1
    print()
    i += 1
print("x"* 40)

# جدول ضرب ۱۰ در ۱۰

i = 0 
while i <= 10:
    j = 0
    while j <= 10:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1

print("x"* 40)

# یک توضییح با استفاده از مثال ستاره

# شکل ساده 
i = 1
while i <= 5:
    print("="* i)
    i += 1

print("x"* 40)

# در زبان های غییر سوسول

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

print("x"* 40)

# تمرین



i = 1


