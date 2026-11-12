from pprint import pprint

class UserList(list["User"]):
    """
!    این کلاس مشتق شده از کلاس لیست و برای توسعه و اضافه کردن 
!    یک قابلیت جدید یه لسیتهاهست 
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


# ساخت کلاس برای seller

class Salesperson(User):

    def order(self, order = "Order") -> None:
        print(f"{self.user_name}: From your products, {order} was sold!")


li = UserList() # مشتق شده از class list
li.append(5)
print(li)

l1 = list()

x = str() # or list , 
print(x)

print(dir(list))

def main():
    ob_1 = User("amir", "amir@gmail.com", "1234")
    ob_2 = User("ali", "ali@gmail.com", "1646")
    ob_3 = User("attila", "aaa@g", "1111")
    print("_"*45)
    # seller_one = Salesperson("ali", "email", "1234")
    # print(seller_one)
    pprint(User.all_user.search("amir"))
    pprint(User.all_user.search("ali mohh"))



if __name__ == "__main__":
    main()
