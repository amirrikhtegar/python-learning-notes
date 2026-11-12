def func():
    print("-" * 40)

# نحوه پیاده سازی
# * composiyion and aggregation


# ! composiyion
class Question:
    def __init__(self, q:str, a:list)-> None:
        self.q = q
        self.a = a

class ExamPeper:
    def __init__(self):
        self.question = Question("what is yuor name?", ["amir", "ali", "mohammad"])

    def __str__(self):
        return f"{self.question.q}\n{self.question.a}"

def main1():
    a = ExamPeper()
    del a
    a.question

# ! aggregation

class Student:
    def __init__(self, name, num):
        self.name = name
        self.num = num

class Universite:
    def __init__(self, students):
        self.students = students

def main2():
    st = [Student("amir", "345"), Student("attila", "123")]
    universite = Universite(st)
    for s in universite.students:
        print(s)

