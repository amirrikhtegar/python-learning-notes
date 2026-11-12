
# * getter, setter

class Color:
    def __init__(self, RGB, name):
        self._RGB = RGB

        if name:
            self._name = name
        else:
            raise ValueError(f"Invalid name {name!r}")

    def set_name(self, name):
        if name:
            self._name = name
        else:
            raise ValueError(f"Invalid name {name!r}")

    def get_name(self):
        return self._name

    def set_rgb(self, RGB):
        self._RGB = RGB

    def get_rgb(self):
        return self._RGB
    

c_fa = Color(0x6783F5, "Light blue")
print(c_fa._name)


c_fa.set_rgb(0x091B66)
c_fa.set_name("blue")


print(c_fa.get_name(), c_fa.get_rgb())

print("*"*45)

# * property methode


class Color:

    def __init__(self, RGB, name):
        self.RGB = RGB

        if name:
            self.name = name
        else:
            raise ValueError(f"Invalid name {name!r}")

    def _set_name(self, name):
            if name:
                self._name = name
            else:
                raise ValueError(f"Invalid name {name!r}")
    
    def _get_name(self):
        return self._name
    
    def _set_rgb(self, RGB):
        self._RGB = RGB
    
    def _get_rgb(self):
        return self._RGB

    name = property(_get_name, _set_name)
    RGB = property(_get_rgb, _set_rgb)


c_fa = Color(0x6783F5, "Light blue")

c2 = Color(0x091B66, "blue")

c2.name = "red"
print(c2.name, c2._RGB)



print('-'* 40)

class Color:

    def __init__(self, RGB, name):
        self._RGB = RGB

        if name:
            self.name = name
        else:
            raise ValueError(f"Invalid name {name!r}")
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError(f"Invalid name {value!r}")
        self._name = value
    
    @property
    def rgb(self):
        return self._RGB

    @rgb.setter
    def rgb(self, rgb):
        self._RGB = rgb


c_fa = Color(0x6783F5, "Light blue")

c2 = Color(0x091B66, "blue")

c2.name = "red"
print(c2.name, c2.rgb)

# * @property

print(dir(property))

print('-'* 40)

class Color1:

    def __init__(self, RGB, name):
        self._RGB = RGB

        if name:
            self.name = name
        else:
            raise ValueError(f"Invalid name {name!r}")
    
    def _getname(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            return self._name
        except:
            return "no has attr name"
    
    def _setname(self, value):
        if not value:
            raise ValueError(f"Invalid name {value!r}")
        self._name = value

    def _delname(self):
        x = input("[Y]es or [N]o: ")
        print(x)
        if x.upper() == "Y":
            del self._name
        else:
            print("not delete attr")

    name = property()
    name = name.getter(_getname)
    name = name.setter(_setname)
    name = name.deleter(_delname)
    
    # or
    #name = property(fset=_setname, fget=_getname, fdel=_delname)

c_fa = Color1(0x6783F5, "Light blue")

c_fa.name = "cyan"
print(c_fa.name)
del c_fa.name
print(c_fa.name)

#help(c_fa) # docstring on getter name

print(" *_* " * 10, "\n")

class Color2:

    def __init__(self, RGB, name):
        self._RGB = RGB

        if name:
            self.name = name
        else:
            raise ValueError(f"Invalid name {name!r}")

    @property
    def name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            return self._name
        except:
            return "no has attr name"

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError(f"Invalid name {value!r}")
        self._name = value

    @name.deleter
    def name(self):
        x = input("[Y]es or [N]o: ")
        print(x)
        if x.upper() == "Y":
            del self._name
        else:
            print("not delete attr")


c_fa = Color2(0x6783F5, "Light blue")

c_fa.name = "cyan"
print(c_fa.name)
del c_fa.name
print()

# کی از property , attr
# کی از attr, property

print(" *_* " * 10, "\n")

# list class

lst1 = [1, 2, 3, 4, 5]

class NewList(list):
    
    @property
    def ave(self):
        return sum(self)/len(self)



ls2 = NewList((1, 2, 3, 4, 5))
print(ls2.ave)


print("*" * 30)

from math import pi

class Circle:

    def __init__(self, radius):
        self._radius = radius
        self._area = 0
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("value lass than or equal zero")

    @property
    def area(self):
        self._area = (self._radius ** 2) * pi
        return f"{self._area:.2f}"
    
ci = Circle(2)
ci.radius = 1
print(ci.area)

class Teperature:
    # fahrenheit
    def __init__(self, tamp):
        self._tamp = tamp
        self._count = 1
    
    @property
    def tamp(self):
        self._count = 2
        self._tamp = (self._tamp * 9/5) + 32
        return f"{self._tamp} F°"

    def show(self):
        if self._count == 1:
            return f"{self._tamp} C°"
        else:
            return f"{self._tamp} F°"



te = Teperature(30)

print(te.show())

print(te.tamp)

print(te.show)
