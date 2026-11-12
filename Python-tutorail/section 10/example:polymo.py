def stare():
    i = 1
    while True:
        if i <= 4:
            print("*" * i)
            i += 1
        else:
            break


class Vehicle:
    def __init__(self, name="", model="", color="", year="", mov="", stp="", s=""):
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.mov = mov
        self.stp = stp
        self.s = s

    def move(self):
        return f"how to move? move by {self.mov}"

    def stop(self, stp=""):
        if stp == "":
            return f"how to stop? stop by {self.stp}"
        else:
            "not stop"

    def sound(self):
        return f"what's sound it make? make {self.sound}"


class Car(Vehicle):
    def __init__(self, name="", model="", color="", year=""):
        super().__init__(name, model, color, year)

    def license(self, li):
        self.li = li
        return f"my license for use this {self.model} it's {self.li}."


class Bike(Vehicle):
    def __init__(self, name="", model="", color="", year=""):
        super().__init__(name, model, color, year)


class Airplane(Vehicle):
    def __init__(self, name="", model="", color="", year=""):
        super().__init__(name, model, color, year)


car1 = Car("benz", "c class", "black", "1997")

bike1 = Bike("giant", "xtc slr 2", "green", "2025")

airplane1 = Airplane("bous", "749", "white", "2000")

j = 0

for i in (car1, bike1, airplane1):
    if j > 0:
        stare()
    j += 1

    print(i.move())
    print(i.stop())
    print(i.sound())
    print("hi")
