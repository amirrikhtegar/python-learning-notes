from pprint import pprint
#* init

# برای init ها از مقدار دهی دقیق با دیکشنری استفاده میکنیم 
#? **kwargs


class BaseClass:
    num_base_calls = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def call_me(self):
        print("calling Base")
        self.num_base_calls += 1

class LftSubClass(BaseClass):
    num_left_calls = 0

    def __init__(self, c, d, **kwards):
        super().__init__(**kwards)
        self.c = c
        self.d = d

    def call_me(self):
        super().call_me()
        print("calling Left")
        self.num_left_calls += 1

class RightSubClass(BaseClass):
    num_right_calls = 0

    def __init__(self, e, f, g, **kwards):
        super().__init__(**kwards)
        self.e = e
        self.f = f
        self.g = g


    def call_me(self):
        super().call_me()
        print("calling Right")
        self.num_right_calls += 1


class SubClass(LftSubClass, RightSubClass):
    num_sub_calls = 0

    def __init__(self,h, u, **kwards):
        super().__init__(**kwards)
        self.h = h
        self.u = u

    def call_me(self):
        super().call_me()

        print("calling Sub")
        self.num_sub_calls += 1



o = SubClass(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, u=9)

o.call_me()
pprint(SubClass.__mro__)
print(o.num_base_calls, o.num_left_calls, o.num_right_calls, o.num_sub_calls)
print(o.a, o.b, o.c, o.d, o.e, o.f, o.g, o.h, o.u)



# اجرا تمام چیز های یاد گرفته روی یک کلاس به نام user

from pprint import pprint



class UserList(list["User"]):

    def search(self, user_name:str) -> list["User"]:
        matching_users:list["User"] = []
        for user in self:
            if user_name in user.user_name:
                matching_users.append(user)
        
        if matching_users != []:
            return matching_users
        else:
            return "not found"

    def append(self, object):
        if not isinstance(object, User):
            raise TypeError("This list only accepts User")
        return super().append(object)



class User(object):
    
    all_user: list["User"] = UserList()
    def __init__(self, user_name:str, email:str, password:str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.user_name = user_name
        self.email = email
        self.password = password
        User.all_user.append(self)

    def __repr__(self):
        return f"{type(self).__name__}({self.user_name!r}, {self.email!r}, {self.password!r})"

    def __str__(self):
        return f"{self.user_name}"


class Salesperson(User):
    def __init__(self, shaba, **kwargs):
        super().__init__(**kwargs)
        self.shaba = shaba

    def order(self, order = "Order") -> None:
        print(f"{self.user_name}: From your products, {order} was sold!")


class Buyer(User):
    def __init__(self, phone:str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.phone = phone
        

    def __repr__(self):
        super().__repr__()
        return "Buyer"


#?  phone, user_name, email, password, shaba = **kwargs
class SalesAndBuyer(Salesperson, Buyer):
    def __init__(self, score, **kwargs):
        super().__init__(**kwargs)
        self.score = score

    def __repr__(self):
        return f"{type(self).__name__}({self.user_name!r}, {self.email!r}, {self.password!r}, {self.shaba!r}, {self.phone!r}, {self.score!r})"


def main():
    buyer_one = Buyer(phone="0930***", user_name="amir", email="amir@gmail.com", password="1234")    
    saler_one = Salesperson(user_name="amir", email="amir@gmail.com", password="1234", shaba="ir12")
    SandB = SalesAndBuyer(user_name="ali", email="amir@gmail.com", password="1234", shaba="ir123", phone="0901", score="123")
    print(repr(SandB))
    SandB.order("hi")

if __name__ == "__main__":
    main()
    