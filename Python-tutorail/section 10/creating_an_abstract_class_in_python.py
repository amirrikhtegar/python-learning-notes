# Abstract Base Class

from abc import ABC, abstractmethod, ABCMeta





# ? روش دوم 

# print(type(ABC))


# class vehicle(metaclass=ABCMeta):

#     @abstractmethod
#     def move(self):
#         """this method should be implemented"""

#     @abstractmethod
#     def repair(self):
#         """_summary_"""


#     @staticmethod
#     @abstractmethod
#     def func():
#         pass

#     @classmethod
#     @abstractmethod
#     def cla(cls):





#* روش اول 
class Vehicle(ABC):

    @abstractmethod
    def move(self):
        """this method should be implemented"""
        print("default")
    
    @abstractmethod
    def repair(self):
        """_summary_"""
        print("default")

    def class_name(self):
        print(self.__class__)


#! obj = Vehicle()#Can't instantiate abstract class Vehicle without an implementation for abstract methods 'move', 'repair'

# ? Can't instantiate abstract class X without an implementation for abstract methods 'y', 'z'

class Land(Vehicle):

    @abstractmethod
    def num_wheel(self):
        pass

class Air(Vehicle):

    @abstractmethod
    def eject(self):
        pass

class Car(Land):
    def move(self):
        print("driving...")
        super().move()

    def repair(self):
        print("under repair...")

    def num_wheel(self):
        print(4)

c = Car()
c.class_name()
c.move()
c.repair()

print("8" * 25)

class AirPlane(Air):
    def move(self):
        print("on air")

    def repair(self):
        print("noting")

    def eject(self):
        print("take out it plane")

a = AirPlane()
a.class_name()
a.eject()
a.move()
a.repair()


#? exercises
print("*"*30, "\n", "*"*30)

# *1
class Employee:

    @abstractmethod
    def calculate_salary(self):
        pass

class HourlyEmployee(Employee):

    def __init__(self, value):
        self.value = value

    def calculate_salary(self):
        return self.value + ((self.value//100)*10)

class SalariedEmployee(Employee):

    def __init__(self, value):
        self.value = value

    def calculate_salary(self):
        return self.value + ((self.value//100)*5)


# *2

class Car:

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class SportsCar(Car):

    def __init__(self, model):
        self.model = model

    def start(self):
        print("start by keylass")

    def stop(self):
        print("stop by Disc brake")


class Sedan(Car):

    def __init__(self, model):
        self.model = model

    def start(self):
        print("start by key")

    def stop(self):
        print("stop by Cup brake")


# *3

class Person:

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    @abstractmethod
    def greet(self):
        pass

    @abstractmethod
    def introduce(self):
        pass


class Student(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age, role)

    def greet(self):
        print(f"hi {self.name}")

    def introduce(self):
        print(f"whats your age? {self.age}" \
        f"Whats your role in school? its {self.role}")


class Techer(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age, role)

    def greet(self):
        print(f"hi {self.name}")

    def introduce(self):
        print(f"whats your age? {self.age}" \
        f"Whats your role in school? its {self.role}")


# test all
# 1
h = HourlyEmployee(1000)
s = SalariedEmployee(1000)
print(h.calculate_salary(), "and", s.calculate_salary())

# 2
c_sp = SportsCar("banz AMG")
c_se = Sedan("Honda acord")
c_sp.start()
c_sp.stop()

c_se.start()
c_se.stop()

# 3
s = Student("ali", 13, "student")
t = Techer("raza", 35, "techer")

s.greet()
s.introduce()

t.greet()
t.introduce()

