# binary
# txt

# open

f = open(file=r"/home/lord/Desktop/Python/section 9/file mod in open and python/note.txt", mode="r")
# or this
# open("note.txt", "r")

print(f) # python objact


# mods for open

# "r" -> فایل متنی , اشاره گر در ابتدا , اگر وجود نداشته باشد ارور میدهد , قابلیت ادیت ندارد

# اگر در قسمت mod چیزی ننویسیم به صورت دیفالت "r" در نظر گرفته میشود
print(f.readline())
#print(f.write()) error 
print(f.read())

# "t" = text file
# "b" = binary file

open(r"/home/lord/Desktop/Python/section 9/file mod in open and python/note.txt", "rb") # biynary read only
#open("note.txt", "rt") # text read only در حالت پایه نیازی به نوشتن t نیست

""" "w" or "wt" -> برای نوشتن و محتوای قبلی پاک میشود و اشاره گر به ابتدای فایل
و اگر فایل نیاشد اول ایجاد میشودو سپس باز
"""
x = open(r"/home/lord/Desktop/Python/section 9/file mod in open and python/note.txt", "w")

# print(x.readline()) error
print(x.write("hi my friend\nyou are a best man\nand you so poor"))

"""
"a" or "at" -> نوشتن در انتهای فایل و اشاره گر در انتهای فایل و اگر فایلی نباشد اول ایجاد و بعد 
باز میشود
"""

d = open(r"/home/lord/Desktop/Python/section 9/file mod in open and python/note.txt", "a")

print(d.write("\namir mohmmad rikhtegarzadeh"))

"""
"x" or "xt" -> برای نوشتن ، فایل های متنتی ، اشاره گر ابتدای فایل ، 
فقط برای ایجاد فایل هست و قابلیت ساخت فایل ندارد
"""

#w = open("note43.txt", "x")

#print(w.write("amir\namiri"))

# w = open(r"/home/lord/Desktop/Python/section 9/file mod in open and python/note.txt", "a") error

"""
    "b" , "rb", "xb", "wb", ... -> برای ساخت یا پردازش فایل باینری مثل 
jpg
"""

"""
"+" , "r+", "x+", ... -> برای هم پردازش و هم نوشتن در فایل 
"""

# "r+" or "rt+" or "r+t" -> هم برای خوندن و هم نوشتن

# "w+" or "wt+" or "w+t" -> هم برای خوندن و هم نوشتن و متن قبلی پاک میشود و اگر فایل وجود نداشته باشد ایجاد میکند 

F = open("note45.txt", "w+")
print(F.write("amir\namiri"))

# "a+" or "at+" or "a+t" -> هم برای خوندن و هم نوشتن و از انتهای فایل شروع میکند

d = open("note45.txt", "+a")

print(d.readline())
print(d.write("amir"))

# "x+" or "xt+" , ... -> در صورت وجود فایل خطا میدهد


# "rb+", ...
# تمام توضیحات برای فایل باینری هم کاربرد دارد

