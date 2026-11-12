# string

print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count',
'encode', 'endswith', 'expandtabs', 'find',
'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 
'isidentifier', 'islower', 'isnumeric',
'isprintable', 'isspace', 'istitle',
'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 
'removeprefix', 'removesuffix', 'replace',
'rfind', 'rindex', 'rjust', 'rpartition', 
'rsplit', 'rstrip', 'split', 'splitlines', 
'startswith', 'strip', 'swapcase', 'title',
'translate', 'upper', 'zfill'
"""

# casefold

s = "AtTila"

print(s.casefold()) # output: attila

# center

s = "Raza"
print(repr(s.center(10))) # output: '   Raza   '
print(repr(s.center(10, "+"))) # output: '+++Raza+++'

# encode

s = "razaسب"
print(s.encode()) # output: b'raza\xd8\xb3\xd8\xa8'

# expandtabs

s = "   amira    ked"

print(repr(s.expandtabs())) # output: '   amira    ked'

# format_map

x = {"x": "amir", "y": "attila"}

print("{x}{y}".format_map(x))

# index

s = "amir"

print(s.index("a")) # output: 0

# isalpha

s = "amir45"

print(s.isalpha()) # false

s = "attila"
print(s.isalnum()) # true

# isascii

s = "akdkf#kofekf%"
print(s.isascii()) # true

# isdecimal, isdigit, isnumeric

s = "123454635"

print(s.isdecimal())

print(s.isnumeric())

print(s.isdigit())

# all true

# isidentifier

s = "a_ddd g"

print(s.isidentifier()) # false

# islower


# isprintable


# isspace

s = "      \n\t\n   "  

print(s.isspace())

# istitle

s = "Amir 01"

print(s.istitle)

# isupper

s = "amir Amifdf"

print(s.isupper())

# ijust, rjust

s = "attila"

print(s.ljust(10))
print(s.rjust(10, "-"))

# maketrans , translate

s = "R.aza...hgfghjk"
table = str.maketrans("a", "à", ".")
print(chr(224))
print(table)
print(s.translate(table))

# or

d = {"a": "-", "z": "+", "R": None}
table = str.maketrans("a", "à", ".")

# or 

c = d.keys()
for i in c:
    print(ord(i))

da = {97: "-", 122: "+", 82: None}
print(s.translate(da))

# partition

s = "amir 01 raza"

print(s.partition("01"))
print(s.rpartition("a"))

# 'removeprefix', 'removesuffix'

s = "-----amir-----"

print(s := s.removeprefix("--"))

print(s.removesuffix("--"))

# split

s = "amir, ali, sgar, karem, hade"

print(s.rsplit(",", 2))
print(s.split(",", 2))

# splitlines

s = "amir,\n ali,\n sgar,\n karem, hade"

print(s.splitlines(True))
print(s.splitlines(False))

# startswith

s = "Amir Ali"

print(s.startswith("A"))

# swapcase

s = "Amir Ali"

print(s.swapcase())

# zfill

s = "Amir Ali"

print(s.zfill(20))

s = b'my name is m\xc3\xb6bius'
print(s.decode("utf-8"))