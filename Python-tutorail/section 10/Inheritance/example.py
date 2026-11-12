class Animal:
    def __init__(self, name_animal:str, species:str) -> None:
        self.name_animal = name_animal
        self.species = species

    def make_sound(self) -> None:
        print("Generic animal sound.")


class Mammal(Animal):
    def __init__(self, num_foot=4, **kwargs):
        super().__init__(**kwargs)
        self.num_foot = num_foot

    def make_sound(self) -> None:
        super().make_sound()
        print("Generic mammal sound.")


class Dog(Mammal):
    def __init__(self, breed, **kwargs):
        super().__init__(**kwargs)
        self.breed = breed

    def make_sound(self) -> None:
        super().make_sound()
        return "Woof!"

    def __str__(self):
        return f"hi, I'm {self.name_animal} and my species {self.species}  and my breed {self.breed} and in the end of this my number foot is {self.num_foot}"


do1 = Dog(num_foot=4, name_animal="Asgar", species="Caniformia", breed="Urocyon cinereoargenteus")

print(do1.make_sound())

print(str(do1))