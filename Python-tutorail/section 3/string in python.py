x = 10
print(isinstance(x, float))

# string in python

s = "Hello, World!"
print(s)
s = 'I\'m'
print(s)
ds = "am\nkldkf"
print(ds)

# \n is used for new line and \\n is used to print \n

print("am\\nkldkf")

# r"" is used to print raw string

print(r"am\nkldkf")

# """""" is used for multi line string

ms = """This is a
multi line
string."""
print(ms)

# \ To cancel the order of special characters

# part 2

X = "This is a long string that spans multiple lines."

# شماره گذاری از صفر شروع میشود
# و منفی از -۱ شروع میشود
# indexing

print(X[0])
print(X[2])
print(X[-2])

# slicing

print(X[0:4])  # Output: This
print(X[-8:-1])  # Output: e lines
print(X[0:2]+X[2:4])  # Output: This
print(X[:5])  # Output: This
print(X[5:])  # Output:  is a long string that spans multiple lines.
print(X[0:10:2])  # Output: Ti  o tig
print(X[::3])  # Output: Ti  tigap ul ie.
print(X[::-1])  # Output: .senil elpitlum taht gnirts gnol a si sihT

# string methods easy

x = "12dikfj111"

print(len(x)) # Output: 7
print(x[4:len(x)]) # Output: kfj
print(x.upper()) # Output: 12DIKFJ111
print(x.lower()) # Output: 12dikfj111
print(x.count("1")) # Output: 3
print(x.endswith("1")) # Output: True
print(x.startswith("1")) # Output: False
print(x.find("d")) # Output: 2
print(x.rfind("1")) # Output: 9
print(x.isalnum()) # Output: False
print(x.isnumeric()) # Output: False کاربردی

d = "*"

tuple = ("apple", "banana", "cherry")

print(d.join(tuple)) # Output: apple*banana*cherry

ds = "reza, ali, hossein"

print(ds.split(",")) # Output: ['reza', ' ali', ' hossein']
print(x.replace("1", "9")) # Output: 92dikfj999
print(x.strip("1")) # Output: 2dikfj
print(x.capitalize()) # Output: 12dikfj111

# Special characters
print("Hello \r World") # Output:  World
print("Hello \t World") # Output: Hello      World
print("Hello \b World") # Output: Hell World
print("Hello \n World") # Output: Hello 
                        #         World
print(ord("A")) # Output: 65
print(chr(65)) # Output: A

# string formatting classic

x = 1.23456
y = 23
print("x :", round(x, 1), "y :", y, sep="--")  # خروجی: x : 1.2--y : 23
print("x is: %i\ny is: %i"%(x, y))

# [(key)] [flag] [w] [.p] type

print("%i" %(2))
print("%c" %(65)) # output: A for character
print("%s" %("Hello")) # output: Hello for string
print("%f" %(1.23456)) # output: 1.234560 for float
print("%d" %(23)) # output: 23 for integer
print("%o" %(23)) # output: 27 for octal
print("%x" %(23)) # output: 17 for hexadecimal
print("%e" %(123456789)) # output: 1.234568e+08 for scientific notation
print("%r" %("Hello")) # output: 'Hello' for representation

print("%.2f" %(1.23456)) # output: 1.23 for float with 2 decimal places
print("%10s" %("Hello")) # output: '     Hello' for string with width 10
print("%9.2f" %(1.23456)) # output: '     1.23' for float with width 9 and 2 decimal places
print("%-6.2f" %(1.23456), "x",sep="") # output: '1.23  x' for left-aligned float
print("%+d" %(23)) # output: +23 for signed integer
print("%08d" %(23)) # output: 00000023 for zero-padded integer with width 8

x = {'name': 'Ali',
    'age': 25}
print("%(name)s" %(x)) # output: Ali for dictionary value with key 'name'
print("%(age)d" %(x)) # output: 25 for dictionary value with key 'age'
p = 10
print("%8.*f" %(p, 1.23456)) # output: '   1.234560' for float with dynamic precision
print("%*.*f" %(p, 3, 1.23456)) # output: '  1.235' for float with dynamic width and precision

# string formatting format()

x = 1.23456
y = 23
z = {
    'a': 1.23456,
    'b': 23,
    'c': x+y
}


print("x is {}\ny is {}\nz is {}".format(x, y, x+y))
print("\n")
print("x is {0}\ny is {1}\nz is {2}".format(x, y, x+y))# with index
print("\n")
print("x is {a}\ny is {b}\nz is {c}".format(a=x, b=y, c=x+y))# with key
print("\n")
print("x is {a}\ny is {b}\nz is {c}".format(a=z['a'], b=z['b'], c=z['c']))# with dictionary
print("\n")
print("x is {a}\ny is {b}\nz is {c}".format(**z))# with dictionary
print("\n")
# {"[field_name][!conversion][:format_spec]"}
# [[fill]align][sign][#][0][width][,][.precision][type]
print("x is {0!r}\ny is {1!s}\nz is {2!a}".format("hello", "amir", "ali"))# output: hello hello 'hello'
print("\n")
print("x is {0:.2f}".format(x))# output: 1.23
print("\n")
print("x is {0:c} {1:d} {2:f} {3:s} {4:o} {5:x} {6:e} {7:%}".format(65, 12, 12.23, "amir", 1234, 234, 100000000, 1.5))
# output: A 23 1.234560 Hello 27 17 1.234568e+08 'Hello' 85.000000%
print("\n")
print("x is {0:.2f} {1:10s} {2:9.2f} {3:-6.2f} {4:+d} {5:08d}".format(1.23456, "Hello*", 1.23456, 1.23456, 23, 23))
# output: 1.23 Hello*        1.23   1.23 +23 00000023
print("\n")
print("x is {0:,.2f}".format(1234567890.12345))# output: 1,234,567,890.12
print("\n")
print("x is {0:_.2f}".format(123467.2345)) # output: x is 123_467.23
print("x is {0:*^8,.2f}".format(1.222234)) # output: x is **1.22**
print("x is {0:#b} {0:#o} {0:#x}".format(123)) # output: x is 0b1111011 0o173 0x7b
print("x is {0:*^+} {1:*^-} {2:*^ }".format(23, 12, -11)) # output: x is +23 12 -11
print("x is {0:^010}".format("hi")) # output: x is 0000hi0000
print("x is {:->20s}".format("hello")) # output: x is ---------------hello
ssd = int(input("enter your pi:"))
print("ssd is {0:{fill}{align}{width}}".format("hello", align = "^", fill = "*", width = ssd)) # dynamic fill, align, width , output: *****hello*****

# f-string formatting best metod (python 3.6+)

x = 112
y = 23
z = "attila"
u = "amir"

print(f"x is {x}\ny is {y}\nz is {x+y}")

print(f"x is {z!s}\ny is {u!r}\nz is {z+u!a}") # output: attila 'amir' 'attilaamir'

print(f"x is {x:*^10.2f}") # output: x is ***1.23****

print(f"x is {y:+d}") # output: x is +23

print(f"x is {10000000:,.2f}") # output: x is 10,000,000.00

print(f"x is {{{x}}} , y is {{y}}") # output: x is {1.23456} , y is {y}

print(f"x is {x:#b} {x:#o} {x:#x}") # output: x is 0b1 0o1 0x1

print(f"x is {y:*^+} {12:*^-} {-11:*^ }") # output: x is +23 12 -11

def f(s):
    return s.upper()
print(f"x is {f('hello')}") # output: x is HELLO

name = "amir"
print(f"hello {name.upper()}") # output: hello AMIR
print(f"hello {name.replace('amir', 'ali')}") # output: hello ali

msg = (
    f"Hello {name},\n"
    f"Welcome to the world of Python f-strings!\n"
    f"Your name in uppercase is {name.upper()}.\n"
    f"Have a great day!"
)

print(msg) # output: Hello amir,\n Welcome to the world of Python f-strings!\n Your name in uppercase is AMIR.\n Have a great day!

msd = f"""This is a multi-line
f-string example
Hello {name},
Your name reversed is {name[::-1]}.
"""
print(msd) # output: This is a multi-line\n f-string example\n Hello amir,\n Your name reversed is rima.

import datetime

now = datetime.datetime.now()

print(f"Current date and time: {now:%Y-%m-%d %H:%M:%S}") # output: Current date and time: 2024-06-15 12:34:56
print(f"Current date: {now:%Y}") # output: Current date: 2025



