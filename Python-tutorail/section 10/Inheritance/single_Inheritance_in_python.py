from pprint import pprint

# * Single Inheritance
# ? IS_A

# ! ساختار کلی

class Parent:
    pass

class Child(Parent):
    pass

# مثال 

class Animal:
    def speek(self):
        print("Anmail makes a sound")

class Dog(Animal):
    def bark(self):
        print("Woof, woof!")

#? تمام کلاس ها از کلاس obj ارث بری کردن 

print(Animal.__base__) # <class 'object'>

class Parent(object):
    pass

#!----------------------!
#* مثال مدرس

class User:
    all_user: list["User"] = [] # public attribute
    def __init__(self, user_name:str, email:str, password:str) -> None:
        self.user_name = user_name
        self.email = email
        self.password = password
        User.all_user.append(self)

    def __repr__(self):
        return f"{type(self).__name__}({self.user_name!r}, {self.email!r}, {self.password!r})"

    def __str__(self):
        return f"{self.user_name}"


# ساخت کلاس برای seller

class Salesperson(User):

    def order(self, order = "Order") -> None:
        print(f"{self.user_name}: From your products, {order} was sold!")



def main():
    #!  از کلاس اصلی
    ob_1 = User("amir", "amir@gmail.com", "1234")
    print(repr(ob_1))
    #? print(ob_1.order()) در کلاس user وجود ندارد و مربوط به کلاس مشتق شده است.
    ob_2 = User("ali", "ali@gmail.com", "1646")

    print("_"*45)
    
    seller_one = Salesperson("ali", "email", "1234")
    print(Salesperson.__base__)
    
    print(repr(seller_one)) #! ارث بری از کلاس پرنتس
    print(seller_one.all_user) #! ارث بری از کلاس پرنتس

    seller_two = Salesperson("attila", "attila@gmail.com", "1646")

    print(seller_one.order()) # متود خود کلاس

    pprint(User.all_user) #  برای اثبات مشتق شدن کلاس فروشنده از user

if __name__ == "__main__":
    main()
