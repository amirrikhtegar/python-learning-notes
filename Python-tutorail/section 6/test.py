l = []

def func():

    yield 
    yield 1

g = func()


print(next(g))
g.send(5)