# walurs operator
# example


print(w := 5)

#++++ example one

x = []

s = input("namxe: ")
while s.lower() != "q":
    x.append(s)
    s = input("name: ")

print(x)

# بهینه تر

y = []

while True:
    s = input("name: بهینه")
    if s.lower() == "q":
        break
    y.append(s)

print(y)

# بهینه تر تر 

r = []

while (s := input("name: q for quit: ").lower() != "q"):
    r.append(s)

print(r)

# ++++++ example two

a = [1, 2, 3, 4, 5]
if (n := len(a)) > 3:
    print(n)


def func(x:int):
    print(x**2)


func(z := 5)

print(z)

# ++++++ example three

f = lambda x: (c := x**2)

# +++++ example four

x = [1, 2, 3, 4]


d = {
    "len" : (l := len(x)),
    "sum" : (s := sum(x)),
    "avg" : l / s
}

print(d)


# extrsize

for _ in range(10):
    if len(s := input("name: ")) > 10:
        print(s)
        break
    else:
        break

# -----------

if len(l := [1, 2, 3, 4, 5, 6, 7])-1 >= 5:
    print(f"xxx{l[0] + l[1]}xxx")


# -----------1----------

if (length := len(s := input("یک رشته وارد کنید: "))) > 10:
    print(f"طول رشته بیشتر از ۱۰ است طول آن: {length}")
else:
    print(f"طول رشته کمتر از ۱۰ است طول آن: {length}")

# -----------2-----------
 
if(length1 := len(list_elements := [7, 2, 5, 6, 1, 7, 4, 10, 3])) > 5:
    sum_first_tow = list_elements[0] + list_elements[1]
    print(f"جمع دو عنصر اول: {sum_first_tow}")
else:
    print(f"طول کمتر از 5 است طول آن: {length1}")

# -----------3-----------

total_sum = 0
while (user_input := input("یک عدد وارد کنید: ")) != ("" or " "):
    number = float(user_input)
    total_sum += number
    print(f"مجموع فعلی : {total_sum}")


# -----------4-----------


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
target = 5
for i, num in enumerate(numbers):
    if (found := num) == target:
        print(f"number {target} in index {i}")
        break
    else:
        print(f"number not in list {target}")

# -----------5------------

from random import randint

count = 0

while (num := randint(1, 100) <= 80):
    count += 1
    print(f"Generated number {num}")


print(f"{num} number bigest than 80")
print(f"number of generated number: {count}")

# -------------6--------------

if (words := ((sentence := input("pleas writing a sentence: ")).split())):
    count = len(words)
    print(f"Number of words in a sentence: {count}")
else:
    print("Please enter a valid sentence.")
