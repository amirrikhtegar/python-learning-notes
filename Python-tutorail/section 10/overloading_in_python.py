def A():
    print("*" * 40)
    print("*" * 40)


# * over loading

print(1 + 1) # 2
print("1" + "1") # "11"
A()
# ? به اینکه یک عملگر در مواجه با تایپ های متفاوت رفتار مخصوص به خودش را نشان میدهد 

print(dir("a"))
A()
print(dir(2))


# in class

class Person:

    def __init__(self, name, age, ad_card):
        self.name = name 
        self.age = age
        self.ad_card = ad_card

    def __str__(self):
        return f"my name is {self.name}, my age is {self.age}"

    def __repr__(self):
        return f"{type(self).__name__}({self.name!r}, {self.age})"

    def __add__(self, other):
        return (self.age + other.age), (self.name + other.name)

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age < other.age

    def __eq__(self, value):
        return self.ad_card == value.ad_card



p1 = Person("smir", 20, "123")
p2 = Person("amir", 19, "456")
# print(p2 + p1) unsupported operand type(s) for +: 'Person' and 'Person'
print(p2 + p1)
print(p2 < p1)
print(p2 > p1)
print(p2 == p1)