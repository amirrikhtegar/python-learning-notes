from random import sample, randint, choice 
l = ["a", "b", "c", "d"]

for _ in range(4):
    print(choice(l))



print(sample(l, 2))