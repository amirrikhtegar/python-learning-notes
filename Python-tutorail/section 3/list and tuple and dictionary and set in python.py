# list in python

# انواع روش ساخت لیست

studant = ["raza", "dolate", 12, 15, 16]
print(studant, "\n", type(studant)) # output: ['raza', 'dolate', 12, 15, 16] \n  <class 'list'>

number = list("reza")
print(number, "\n", type(number))  # output: ['r', 'e', 'z', 'a'] \n  <class 'list'>

s = "a l i m o"
ch = s.split(" ")
print(ch, "\n", type(ch)) # output: ['a', 'l', 'i', 'm', 'o'] \n  <class 'list'>

# slicing 
print(studant[0]) # output: raza
print(studant[1:4:1]) # output: ['dolate', 12, 15]
print(studant[::1]) # output: ['raza', 'dolate', 12, 15, 16]

# + * ,,,,

list_1 = [1,2,3,4,5,6]
list_2 = [7, 8, 9]

print(list_1 * 2) # output: [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
print(list_1 + list_2) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# تغییر عضو در list
# mutable and immutable
 
list_1[0] = 10
print(list_1) # output: [10, 2, 3, 4, 5, 6] , mutable

# برابری در لیست
list_1 = [1,2,3,4,5,6]
list_3 = [1,2,3,4,5,6]
list_4 = [2, 1, 3, 4, 5, 6]
print(list_1 == list_3) # output: trua
print(list_1 == list_4) # output: false
print(2 in list_2) # output: false

# ذخیره سازی در حافظه 
l1 = [1, 2, 3, 4, 5]
l2 = l1
print(id(l1))
print(id(l2))

l2 = l1[:]

l2 = l1.copy()

# list های تو در تو 

list21 = [1 ,2 ,3 ,[1, 3, 4]]
print(list21[3][1])

listr = [1, 32 ,3, ["sdfg", "ssdd"]]
print(listr[3][1][1])

# کپی لیست تو در تو 

listr = [1, 32 ,3, ["sdfg", "ssdd"]]
l2 = listr.copy()
print(id(listr))

print(id(l2))

l2[3][1] = "0"

print(listr)
print(l2)
# shallow copy ^

# deep copy> 

import copy

listr = [1, 32 ,3, ["sdfg", "ssdd"]]

l2 = copy.deepcopy(listr)

print(id(listr))

print(id(l2))

l2[3][1] = "0"

print(listr)
print(l2)

# metode append
l = [1, 2, 3, 4, 5]
l.append("df")
l.append(["amir", "ali"])
print(l) # output: [1, 2, 3, 4, 5, 'df', ['amir', 'ali']]

# با استفاده از slising

l[1:3] = ["A", "B", "C"]
print(l) # output: [1, 'A', 'B', 'C', 4, 5, 'df', ['amir', 'ali']]

a, b, *c = [1, 2, 3 ,4]
print(a) #1
print(b) # 2
print(c) #[3, 4]

del c

# tuple in python 

tuple_1 = (1, 2, 3, [1, 2, 3])
# tuple_1[1] = 1 error 
t = 1 ,2 ,3 ,4
print(type(t)) # tuple

print(tuple_1[1:4])

tuple_1[3][1] = "amir"
print(tuple_1) # (1, 2, 3, [1, 'amir', 3])

x = []
print(x)
x.append("a")
print(x)
x = tuple("input enter your tuple: ")

print(x)
a, b, *c = (1, 2, 3, 4, 5)
print(c)

# dictionary in python

d = {}
print(type(d))

d1 = {"a":1,"b":2}
# this is a dictionary , keys and values
print(d1["a"]) # output: 1

# key immutable
# value all type

d2 = {(1, 2, 3):[1, 2, 3, 4]}

d_f = {"a": {1: 2}}

d_e = {1:2, 2: 3, 1:4}
print(d_e[1]) # output: 4

d4 = {"a":1, "b":2, "c":3}
print(d4)
d4["a"] = 22 # chang value
print(d4)
d4["d"] = 23 # Add key and value
print(d4.get("f")) # none

print(list(d4.keys())) # ['a', 'b', 'c', 'd']
print(list(d4.values())) # [22, 2, 3, 23]
print(type(d4.items())) # <class 'dict_items'>
print(type(list(d4.items()))) # <class 'list'>
print(list(d4.items())) # [('a', 22), ('b', 2), ('c', 3), ('d', 23)]

del d_f
# print(d_f) error

x = d4["a"]
#del d["a"]
d["x"] = x

# chang key
l = [1, 2, 3, 5, 4]
print(sorted(l)) # مرتب کردن

print(sorted(d4.keys())) # ['a', 'b', 'c', 'd']
print(sorted(d4.values())) # [2, 3, 22, 23]
# مرتب کردن کلید و ولیو

x = dict([("d", 2), ("b", 23)])
y = dict(a= 10, b= 20)
# d = {x : x**2 for i in range(10)}
print(d) 

danshjo = {
    "172" : {"name" : "ali" ,  "age" : 24},
    "156" : {"name" : "amir" ,  "age" : 25}
}

print(danshjo["156"]["name"])
y = ("a", "b", "c", "d")
x = (1, 2, 3, 4)
z = dict(zip(y, x))
print(z) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# set in python

s = {1, 2, 3, 4}
print(type(s))
print(id(s))
s.add(4)
print(s) # {1, 2, 3, 4}
print(id(s)) # id (s) = (s.add)
# print(s[1]) # error


# compane = {""}
#compane = set()
#x = input("name: ")
#y = input("name: ")
#t = input("name: ")
#s.add(x)
#s.add(y)
#s.add(t)
#print(s)

# s.remove(8) # یک error میده اگر عضو نباشه
s.discard(8) # اگر عضو نباشه error نمیده

print(len(s)) # تعداد عضو ها
print(3 in s) # true
# تعریف دومجموعه 
p = {3, 9, 15, 12, 6, 18}
q = {12, 6, 18, 10, 4, 26, 2}
# منها کردن در مجموعه
print(p-q) # {9, 3, 15}
print(p.difference(q)) # {9, 3, 15}
# اجتماع گرفتن
print(len(p | q))
print(p | q) # {2, 3, 4, 6, 9, 10, 12, 15, 18, 26}
print(p.union(q)) # {2, 3, 4, 6, 9, 10, 12, 15, 18, 26}
# اشتراک گرفتن
print(q & p) # {18, 12, 6}
print(p.intersection(q))
# تفاضل متقارن
print(p ^ q) # {2, 3, 4, 9, 10, 15, 26}
print(p.symmetric_difference(q))
# زیر مجموعه
a = {40, 50, 20, 10, 30, 60}
b = {10, 30, 60}
print(a > b) # True
print(a < b) # False
print(a.issubset(b)) # False
print(a.issuperset(b)) # True

# example for dict, list and set

# example one
marks = []
name = input("name: ")
marks.append(name)
fizik = float(input("mark: "))
marks.append(fizik)
math = float(input("mark: "))
marks.append(math)
thran = float(input("mark: "))
marks.append(thran)
print(marks)
ave = (marks[1] + marks[2] + marks[3]) // 3
print(ave)
# output :
# name: amir
# mark: 13.5
# mark: 15
# mark: 20
# ['amir', 13.5, 15.0, 20.0]
# 16.0

# example two

phone = input("phone: ")
digit_list = list(phone)
print(digit_list)

# example three

l1 = [1, 2, 3]
l2 = ["a", "b", "c"]
l1[-1:] = l2
l1[-1] = l2
print(l1)

# example four

marks = {}
name = input("neme: ")
m = float(input("mark: "))
marks[name] = m

name2 = input("neme: ")
m2 = float(input("mark: "))
marks[name2] = m2

print(marks)

# example five

s = input("jdkf")
chs = set(s)
print(chs)
print(len(chs))

# Practice
# 1
dicttionary = {}

key = input("word: ")
meanings = input("meanings: ").split(",")

key2 = input("word: ")
meanings2 = input("meanings: ").split(",")

dicttionary[key] = meanings
dicttionary[key2] = meanings2
print(dicttionary)

# 2
word = input("your word: ")
# print("miney: ", dicttionary.get[word])
