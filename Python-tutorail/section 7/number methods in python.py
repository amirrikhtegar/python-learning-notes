# number metodes

# متود های داخلی

print(divmod(10, 2)) # (5, 0)

print(pow(10,2,2))  # output: 0

print(round(12.2345678, 3)) # output: 12.235

print(abs(-546)) # output: 546

# متود های مهم intger

x = 2
print(dir(int))

print(x.as_integer_ratio()) # output: (3, 4)

print(x.bit_count())

y = 5 + 4j

print(y.conjugate())
print(y.imag)
print(y.real)

print(format(255,"x")) 

print((5).__or__(2))
print(x.__or__(2))
print(x.__invert__())