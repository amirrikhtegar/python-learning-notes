from math import hypot
from time import sleep
#import typing import Optional

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
    def __init__(self, x: float | int=0, y:float=0) -> None:
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


# روش قدیمی 
# برای تست با mypy
#ob_p1 : Optional[Point] = None
# روش از ۳.۱۰ به بعد
ob_p1 : Point | None = None


# تابع برای کنترل ساخت ابجکت

def get_obj():
    global ob_p1
    if not ob_p1:
        ob_p1 = Point()
    # sleep(5) # برای شبیه سازی طولانی بودن ساخت ابجکت
    return ob_p1


def get_obj_b():
    global ob_p1

    if ob_p1 is None:
        ob_p1 = Point()

    return ob_p1

# مدریت ابجکت و اسکریپت

def main():
    print("clucator")
    po1 = get_obj_b()
    po1.move(4, 6)

if __name__ == "__main__":
    main()

print("hi")


