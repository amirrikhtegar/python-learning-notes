# buffer
import os

f = open("note_buffer.txt", "w", encoding="utf-8")
f.write("reza\ndolati")

f.flush()
os.fsync(f)
f.write("\nattila")

input("X : ")

f.close()

# part 2

# buffering

# buff = 0

f = open("note.txt", "wb", buffering=0)

f.write(b"reza\ndolati")

input("X : ")

f.close()

# buff = 1

f = open("note.txt", "w", buffering=1)
f.write("reza\ndolati")
f.write("amir\namiri")
input("x: ")
f.close()

# buff = -1

f = open("note.txt", "w", buffering=1)
f.write("reza\ndolati")
f.write("amir\namiri")
input("x: ")
f.close()

import io
print(io.DEFAULT_BUFFER_SIZE)

# buff = chose

f = open("note.txt", "wb", buffering=4)
f.write(b"reza\ndolati")
f.write(b"amir\namiri")
input("df: ")
f.close()

# 

f = open("note.txt", "r", encoding="utf-8")
print(f.readline(6))