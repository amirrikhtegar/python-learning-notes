# args errors

# f = open("note.txt", "w", encoding="utf-8", errors="strict")
# f = open("note.txt", "w", encoding="utf-8", errors="ignori")
# f = open("note.txt", "w", encoding="utf-8", errors=",...")

# args newline

f = open("note.txt", "w", encoding="utf-8", newline="\n") 
f = open("note.txt", "w", encoding="utf-8", newline=None) 

# args closefd & fileno

# f = open("note.txt", "w", encoding="utf-8", closefd=False) # or True 

f.fileno

f.close

# importin method

x = open("note.txt", "w", encoding="utf-8", newline="\n") 
x.write("at\nat\n")
x.truncate(3)

print(x.seekable())

import os

if os.path.exists("atti.txt"):
    z = open("atti.txt", "r")
    print(z.readlines())

os.remove("note.txt")
