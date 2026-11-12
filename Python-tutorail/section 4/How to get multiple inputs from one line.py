# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))

x, y, *z = input(": ").split(" ")
x = [int(x) for x in input("x , y, z: ").split(" ")] # حل کردن مشکل فرمت متغییر
print(30 * "-")
print("x=", x, "\ny=", y, "\nz=", z, sep=",")

