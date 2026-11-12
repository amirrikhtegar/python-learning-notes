
# * docstring

from math import hypot


class Point:
    """
    A point on the axis provides tow-dimensional coordinates.
    # example
    >>> p1 = Point()
    >>> p2 = Point(3, 4)
    >>> p2.reset()
    >>> p1.distance(p2)
    0.0
    """
    #methods: 
    #move: 
    #attribute ->  attribute -> default / non default
    def __init__(self, x:float=0, y:float=0) -> None:
        """
        Initialize the x and y coordinates
        :param x: x-coordinates
        :param y: y-coordinates
        return : None
        """
        self.x = x
        self.y = y
        #self.move(x,y)
        # نباید retern داشته باشد
    def move(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        print(self)
        self.move(0, 0)

    def distance(self, other:"Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)

ob_p1 = Point(3, 4)
ob_p2 = Point(0, 0)
ob_p3 = Point()
print(ob_p3)

print(ob_p1.distance(ob_p2))
print(ob_p3.distance(ob_p1))


# نحوه استفاده از docstring

print(Point.__doc__)

print(help(Point()))
print(help(enumerate))

import doctest

doctest.testmod()

# mypy test.py

# رایج ترین سبک های نوشتن docstring

