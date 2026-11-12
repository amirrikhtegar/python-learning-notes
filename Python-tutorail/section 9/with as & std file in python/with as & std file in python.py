# context manager
    # __enter__
    # __exit

# with expression

class context_manager_for_test:
    def __enter__(self):
        print("start!")

    def __exit__(self, exe_type, exe_val, exe_tb):
        print("end!")

with context_manager_for_test() as s:
    print("i am amir!")
    print("welcome")

print(dir(context_manager_for_test()))

# con 1

f = open("note.txt", "w")
print(dir(f)) # output : __enter__ , __exit__
f.close()

# con 2

f = open("text.txt", "w")
try:
    f.write("amir\namiri")
finally:
    f.close()

# con 3

with open("text.txt", "wb") as f:
    if f.writable():
        f.write(b"hi")

#f.write(b"a") # error -> ValueError :I/O operation on closed file.

# con 4

with open("note.txt", "r") as f:
    with open("new.txt", "w") as s:
        for line in f:
            print(line, end="")
            s.write(line)

# or thet

with open("note.txt", "r") as f, open("new.txt", "w") as s:
    for line in f:
        print(line, end="")
        s.write(line)

# std file

from sys import stderr, stdin, stdout


# stdin -> keyboard ......... input

f = stdin.readline()
print(f"my text in stdin {f}", end="")


# stdout -> screen ......... print

stdout.write(f"my text in stdin and stdout {f}")

# stderr -> screen ......... exc

#print(1 / 0)
stderr.write("Error!")
print("\n***")

# how in file 

stdout_temo = stdout
stdout = open("note1.txt", "w")
stdout.write(f"my text in stdin and stdout in file note {f}")
stdout.close()
stdout = stdout_temo

# or for stdin

stdin_temp = stdin
stdin = open("note1.txt", "r")
f = stdin.readline()
z = input()
print(z)
stdin.close()
stdin = stdin_temp


# argomans for print

print(1, 2, 3, 4, sep=",", end="\t", file=open("note1.txt", "w"), flush=True)
input()