import random
import string

lower, upper = string.ascii_lowercase, string.ascii_uppercase

symbols = "!@#$%^&*()_+=-{}[]:'?><,./\|~`"

numbers = "1234567890"

alls = lower + upper + symbols + numbers

while True:
    print("select your option\n\t1)create a password\t2)exit")
    choice = input("your choice: ")
    
    if choice == "1":
        length = int(input("enter the length of password:  "))
        password = "".join((random.sample(alls, length)))
        print(password)

    elif choice == "2":
        break
    
    else:
        print("your choice is wrong!\n")
