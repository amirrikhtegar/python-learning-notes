lst = []
for i in range(10):
    print(i * 10)

print("\x45")

x = bytearray("سلام", "utf-8")
print(x) 


# !!!!!!!!!!!!!!!!!! مهم نیست

# txt

with open("./note.txt", "rt") as f:
    print(type(f.readline()))



with open("./note.txt", "rt") as f:
    print(f.readline())


# bytes

with open("./Chen.JPG", "rb") as f:
    print(type(f.readline()))


with open("./Chen.JPG", "rb") as f:
    print(f.readline())
