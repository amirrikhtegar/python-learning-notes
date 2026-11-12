# setattr

# *__________

class Shape:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.area = 0
        self.perimeter = 0


    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def show(self):
        info = ""
        for key, value in self.__dict__.items():
            if value > 0:
                info += f"> {key}: {value:.2f}\n"
                
        print(info)

    def __str__(self):
        return f"< {type(self).__name__} >"

# self.langth + self.width
class Rectangle(Shape):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.langth * self.width

    def calculate_perimeter(self):
        self.perimeter = (self.langth + self.width) * 2

# self.langth
class Square(Shape):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.langth ** 2

    def calculate_perimeter(self):
        self.perimeter = self.langth * 4


# base, height, side1, side2
class Triangle(Shape):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = (self.base * self.height) / 2

    def calculate_perimeter(self):
        self.perimeter = self.base + self.side2 + self.side1

# diameter1, diameter2,  
class Parallelogram(Shape):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = (self.diam1 * self.diam2) / 2

    def calculate_perimeter(self):
        self.perimeter = self.length * 4




def rectangle():
    r = Rectangle(langth=2, width=4)
    print(r)
    r.calculate_perimeter()
    r.calculate_area()
    r.show()


