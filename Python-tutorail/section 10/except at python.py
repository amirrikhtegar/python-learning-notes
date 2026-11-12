
# * except *

# !SyntaxError
# while True
#     print("hi")

# ? except

x = int(input("x :"))
y = int(input("y :"))

print("x/y=", x/y) #! x = 1, y = 0 ZeroDivisionError

x = 5
# del x
print(x + 4) # ! exception has occurred: NameError

# ! print("2" + 3) # Exception has occurred: TypeError

x = int(input("x : :"))

print(x + 5) # ! if x = "j" code error: Exception has occurred: ValueError

# ? how to manage except error : try and except


try:
    x = int(input("x2 :"))
    y = int(input("y2 :"))
    print("x/y=", x/y)
    print("End")

except: # if you are a error
    print("pl write true")


# !-------------------------------

try:
    x = int(input("x2 :"))
    y = int(input("y2 :"))
    print("x/y=", x/y)
    print("End")

except ZeroDivisionError: # if you are a error
    print("pl write true")
    y = int(input("y error: "))
    print("x/y=", x/y)

except ValueError:
    print("ValueError")

# !-------------------------------

try:
    x = int(input("x21 :"))
    y = int(input("y21 :"))
    print("x/y=", x/y)
    if y == 10:
        raise NameError("hahahaah error")
    print("ma")
    print("End")

except (ZeroDivisionError, ValueError): # if you are error in except
    print("pl write true")
    y = int(input("y error: "))
    print("x/y=", x/y)
    print("ValueError")

except NameError:
    print("Name error")

else:
    print("End")

finally:
    print("*" * 30)

