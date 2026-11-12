class Person:
    def __init__(self, first_name, last_name, age):
        self.First_name = first_name
        self.Last_nmae = last_name
        self.Age = age

    def __str__(self):
        return f"{self.First_name}, {self.Last_nmae}"

    def __repr__(self):
        #return f"{self.__class__.__name__}('{self.First_name}', '{self.Last_nmae}', {self.Age})"
        return f"{type(self).__name__}({self.First_name!r}, {self.Last_nmae!r}, {self.Age!r})"


p1 = Person("amir", "alimohmmade", 26)
print(str(p1))
print(id(p1))
print(repr(p1))
p2 = Person('amir', 'alimohmmade', 26)
print(str(p2))
print(id(p2))
