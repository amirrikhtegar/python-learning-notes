
class Student:

    def __init__(self, name, age, *scores):
        
        self.name = name
        self.age = age
        self.scores = list(scores)

    def addingـscores(self, *x):
        self.scores.extend(x)
        return self.scores

    def avr_scores(self):
        return round(sum(self.scores) / len(self.scores), 1)



st1 = Student("amir", 17, 12, 18, 20)

print(st1.scores)
print(st1.addingـscores(12 ,3, 2))
print(st1.avr_scores())