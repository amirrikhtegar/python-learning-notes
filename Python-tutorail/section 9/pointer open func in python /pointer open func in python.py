# pointer

f = open("note.txt", "r")

print(f.tell())
print(repr(f.readline()))
print(f.tell())
print(repr(f.readline()))
print(f.tell())
print(repr(f.readline()))
print(f.tell())

x = "attila\nATTIALᏬattila\nattila"

print(len(x))

f.close()


import os

print(repr(os.linesep))

# seek method

f = open("note1.txt", "rb")
print(f.tell())
print(f.read(5))
f.seek(0)
print(f.tell())
print(f.read(5))
print(f.tell())
f.seek(3)
print(f.read(5))
print(f.tell())
f.close()


# آرگومان دوم seek
# 0 -> ابتدای فایل
# 1 -> موقعیت فعلی فایل
# 2 -> انتهای فایل

x = open("text.txt", "rb")
print(x.tell())
print(x.read(3))
x.seek(1)
