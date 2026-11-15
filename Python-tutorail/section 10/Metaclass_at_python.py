
# ! anything in python is object

class Human:
    pass


h = Human()
print(type(h))
print(isinstance(h, Human))

print(Human.__base__)

print("*" * 40)
print(type(Human))

print(type(type))

# mate class

print(isinstance(Human, type))

s = "amir"
print(type(s))
print(isinstance(s, str))
print(isinstance(str, type))


class HumanMeta(type):
    pass

class Human(metaclass=HumanMeta):
    pass

h = Human()
print(type(h))
print(type(Human))

print(dir(type))
