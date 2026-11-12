
class Book:

    def __init__(self, titel, writer, year):
        self.titel = titel
        self.writer = writer
        self.year = year

    def information_book(self):
        return f"This {self.titel} book was written in {self.year} by {self.writer}"


bo1 = Book("grokking algorithm", "Aditya Y. Bhargava", "2015")
print(bo1.information_book())