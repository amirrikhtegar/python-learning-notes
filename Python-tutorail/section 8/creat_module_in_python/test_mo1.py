import creat_module_in_python.creat_module as creat_module

x = creat_module.greet

print(creat_module.greet("علی"))
print(creat_module.add(5, 3))
print(x("attila"))

from creat_module_in_python.creat_module import greet, add, name

print(greet("علی"))
print(add(5, 3))

f = greet

print(f("attila"))

import math

print(math.pi)

print(name)

from creat_module_in_python.creat_module import *

print(globals())

print("*"*35)

import importlib

importlib.reload(creat_module)

print(creat_module.__name__)

