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

