# in python version 2 
# 1. normal string: accii and bynere

print(type("r")) # str

# ver 3 python
# 1. normal string(ascii, unicode) = str type
# 2. bytes = date bynare
# 3.bytearray = date bynere mutabli
#2
s = b"r"
print(type(s))
#1
x = u"r"
print(type(x))
#3
z = bytearray("a", "utf-8")
print(type(z))

# -----------------

name = bytes("razaب", "utf-8")
print(name)
print(type(name))
print("{\xd8\xa8}")
print(name[1])
print(name.decode("utf-8"))

# bytearray

name2 = b"amad"
print(name2, type(name2))


name3 = bytearray([65, 66, 67])
print(name3)
name3[2] = 69
print(name3)

# تمرین

x = b'amir'
