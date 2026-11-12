
class Rectangle:

    def __init__(self, witdth:int, height:int):
        self.witdth = int(witdth)
        self.height = int(height)

    def area(self):
        return f"area of rectangle: {(self.witdth + self.height) * 2}"

    def  perimeter(self):
        return f"perimeter of rectangle: {self.witdth * self.height}"


r_1 = Rectangle(10, 5)

print(r_1.area())
print(r_1.perimeter())
