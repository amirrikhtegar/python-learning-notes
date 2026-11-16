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

    @abstractmethod
    def repair(self):
        """_summary_"""

    def class_name(self):
        print(self.__class__)


#! obj = Vehicle()#Can't instantiate abstract class Vehicle without an implementation for abstract methods 'move', 'repair'

