from star_for_all_pro import A
a = A()
lst = [1, 2, 3]
print("__iter__" in dir(lst))

print("__next__" in dir(lst))

it_lst = iter(lst)

print(next(it_lst))
print(next(it_lst))
print(next(it_lst))
#print(next(it_lst)) # exception: no description

a.stare_twe_line

class NewObj:
    def __init__(self, max_pow):
        self.n = 0
        self.max_pow = max_pow
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= self.max_pow:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration    

n = NewObj(5)

a.stare_one_line

for i in n:
    print(i)

print(n.__iter__())



class Fibonacci:
    def __init__(self, n, max_feb):
        self.n = n
        self.feb = max_feb

    def __iter__(self):
        return self

    def __next__(self):
        def fib(n):
            if n <= 1:
                return n
            return fib(n - 1) + fib(n - 2)
        return fib(self.n)


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(3, 5):
    print(fib(i), end=" ")

a.stare_one_line

c = Fibonacci(2, 5)

print(next(c))
print(next(c))
print(next(c))
print(next(c))