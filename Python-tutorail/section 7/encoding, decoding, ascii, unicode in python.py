# Endcoding , Decoding
# Ascii , Unicode

x = "a"
print(bin(ord(x)))
print(ord(x))

s = input("you: ")
x = []
for i in s:
    print(bin(ord(i)))
    x.append(bin(ord(i)))

print(x)

f = 0
for i in x:
    for j in i:
        f += 1

print(f)

