from pprint import pprint

# * اموزش تغییر رفتار 

class UserList(list["User"]):
    """
?    این کلاس مشتق شده از کلاس لیست و برای توسعه و اضافه کردن 
?    یک قابلیت جدید یه لسیتهاهست 
    """

    def search(self, user_name:str) -> list["User"]:
        matching_users:list["User"] = []
        for user in self:
            if user_name in user.user_name:
                matching_users.append(user)
        
        if matching_users != []:
            return matching_users
        else:
            return "not found"

    #? overriding کردن

    def append(self, object):
        if not isinstance(object, User):
            raise TypeError("This list only accepts User")
        # بدون super انگار داریم تابع بازگشتی مینویسیم
        #! return self.append(object)# Error: maximum recursion depth exceeded
        return super().append(object)



class User(object):
    
    all_user: list["User"] = UserList() # به جای دخیره در کلاس list در کلاسی که خودمان از ان مشتق کردیم ذخیره میکنیم که متود سفارشی دارد

    def __init__(self, user_name:str, email:str, password:str) -> None:
        self.user_name = user_name
        self.email = email
        self.password = password
        User.all_user.append(self)

    def __repr__(self):
        return f"{type(self).__name__}({self.user_name!r}, {self.email!r}, {self.password!r})"

    def __str__(self):
        return f"{self.user_name}"


class Salesperson(User):

    def order(self, order = "Order") -> None:
        print(f"{self.user_name}: From your products, {order} was sold!")


class Buyer(User):
    def __init__(self, phone:str, user_name, email, password) -> None: # ?  overriding
        # self.user_name = user_name
        # self.email = email
        # self.password = password
        # User.all_user.append(self)
        # راه بد
        # ? super        
        #super(Buyer, self).__init__(user_name, email, password)
        super().__init__(user_name, email, password)
        self.phone = phone
        

    def __repr__(self):
        super().__repr__()
        return "Buyer"



def main():
    buyer_one = Buyer("0930***", "amir", "amir@gmail.com", "1234")

    if isinstance(buyer_one, User):
        print(repr(buyer_one), "1")
    elif isinstance(buyer_one, Buyer):
        print(str(buyer_one), "2")
    
    
    user_one = User("amir", "amir@gmail.com", "1234")
    if isinstance(user_one, Buyer):
        print(str(user_one), "1")
    elif isinstance(user_one, User):
        print(repr(user_one), "2")

    # overriding

    li = UserList()
    li.append(user_one)
    li.append(buyer_one)
    #! li.append(4) Error: This list only accepts User


if __name__ == "__main__":
    main()


# * مثال درست حسابی
print("*" * 30)

class First:
    def __init__(self):
        print("first")


class Second(First):
    def __init__(self):
        super().__init__()
        print("second")


class Third(Second):

    def __init__(self):
        super().__init__()
        print("third")


class Fourth(Third):

    def __init__(self):
        super().__init__()
        print("fourth", "that's it")


f = Fourth()



