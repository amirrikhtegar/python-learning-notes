x = open("note.txt", "r+", encoding="utf-8")

# متود های open

# method write

print(dir(x))

x.write("\nᏬ")

print(chr(5100))

f = open("note1.txt", "ab+")

s = b"attila\n"

f.write(s)

sd = bytes("ATTIALᏬ", "utf-8")

f.write(sd)

# method wirteble

if f.writable():
    print(f.write(s))

# method readable

if f.readable():
    print(f.read())

# method writelines

lst = ["amir", "ali", "02"]

x.writelines(lst)

dic = {"amir": 12,
        "ali": 13}

x.writelines(dic)

# method read

g = open("text.txt", "r")

#print(g.read(), end="")

print(g.read(2))

# method readline

print(g.readline(2), end="")
print(g.readline(4), end="")
print(g.readline(), end="")
print(g.readline(), end="")

# method readlines

h = open("text1.txt", "r")

note = h.readlines(1)

print(note)

# or 

for line in open("text1.txt", "r"):
    print("*", line, end="")