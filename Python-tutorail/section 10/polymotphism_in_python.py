def stare():
    i = 1
    while True:
        if i <= 4:
            print("*"* i)
            i += 1
        else:
            break


# * polymotphism

#?  رفتار متفاوت در مواجه با نوع های شی 

print(1 + 2) # 3
print("1" + "2") # "12"
print(2 + 2j + 4j) # (2+6j)

# len

li = [1, 2, 3, 4]
s = "amir"
dic = {"a": 2, "b": 3, "c": 4, "d": 5}

print(len(li))
print(len(s))
print(len(dic))

def add(x, y):
    return x + y

def len_b(x):
    c = 0
    for i in x:
        c += 1 
    return c

print(len_b(dic))
print(len_b(li))

# class polymo..
# چند ریختی در وراثت

class Animal():
    def __init__(self, name="", color=""):
        self.name = name
        self.color = color

    def info(self):
        return(f"hi, I'm a {type(self).__name__} and my name is {self.name} and my coler {self.color}")

    def make_sound(self):
        return "..."




class Cat(Animal):

    def __init__(self, name="", color=""):
        super().__init__(name, color)

    def make_sound(self):
        return "Meow...."



class Cow(Animal):

    def __init__(self, name="", color=""):
        super().__init__(name, color)

    def make_sound(self):
        return "Moo...."

    def info(self):
        return(f"hi, I'm a {type(self).__name__} and my name is {self.name} and my coler {self.color}")



cat1 = Cat("jaki", "black")

cow1 = Cow("Gavi", "brown")

def func(obj):
    print(obj.info())
    print(obj.make_sound())


for amimal in [cat1, cow1]:
    print(amimal.info())
    print(amimal.make_sound())

stare()

func(cat1)
func(cow1)
