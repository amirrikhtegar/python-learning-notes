
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Make co: {self.make}, car model: {self.model}, year: {self.year}"


car1 = Car("banz", "S", "2020")

print(str(car1))