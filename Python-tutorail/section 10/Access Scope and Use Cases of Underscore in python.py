
# * Access Scope

from random import randint

# انواع دسترسی
# Private => فقط از داخل خود کلاس در دسترس است 
# Public => از همه جا قابل دسترس است 
# Protecred => فقط داخل خود کلاس و کلاس های ارث بری شده 
# با مبحث کپسول سازی هم پوشانی دارد 
# سیاست پایتون این است که بهتره از داده پریاوت استفاده نکنی و ولی اگه استفاده کردی حتمی دلیلی داری
class User1:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def _id(self, a, b=1000):
        self._id = randint(a, b)
        return self._id

    def __password(self, password):
        self.__password = password

ob_U = User1("amir", 19)

print(ob_U._id(3))

# underscore
# ۵ حالت 

# ? 1
# استفاده به تنهایی (_)
# برای زمانی که متغییر قرار نیست استفاده شود
for _ in range(10):
    print("Hi")

name, _, _ = ("amir", 19, "A")

print(name)
print(_)

# ? 2
# قبل از (_) اسم یک متغییر یا متد 

# Protecred => _NameAttr or _NameMethod

class User:

    def __init__(self, name : str="", phone : str=""):
        self._user_id = id(self)
        self.name = name
        self.phone = phone

ali = User("ali", "0930")

print(ali._user_id, ali.name, ali.phone, sep="*")

__all__ = ["_x"]
_x = 12

# ? 3

# بعد از اسم از (_) استفاده کرد برای بی اثر کردن اسم های اصلی

min_ = 12
print(min)
print(min_)

# ? 4

# استفاده از دوتا (_)قبل اسم متود و اتربیوت و برای حالت دسترسی محدود و پرایوت هست 
# name mangling

class User3:

    def __init__(self, name : str="", phone : str=""):
        self.__user_id = id(self)
        self.name = name
        self.phone = phone
        self.x = "+" + str(self.__user_id)

ali = User3("ali", "0930")

#print(ali.__user_id, ali.name, ali.phone, sep="*") error 
print(ali.x, ali.name, ali.phone, sep="*")

# برای ارث بری کاربرد دارد

class Account(User3):
    def __init__(self):
        super().__init__()
        self.__user_id = "1234567"

ali_account = Account()


print(ali_account.x, ali_account.name, ali_account.phone, sep="*")
print(dir(ali_account))

# نحوه دسترسی

print(ali._User3__user_id)

# ? 5

# __nameattr__ -> python bulti in methods

# ? get , set
# برای زمانی که میخواهیم به


class User4:

    def __init__(self, name : str="", phone : str="___"):
        self.name = name
        self.__phone = phone
        self.user_id = id(self)
    def set_phone(self, phone):
        if len(phone) == 11 and phone.isdigit():
            self.__phone = phone

    def get_phone(self):
        return self.__phone

ali = User4()
ali.set_phone("090116035570")
ali.set_phone("090116033_0")
number = ali.get_phone()
print(number)

# روش جدید 

class Person:
    def __init__(self, age="--"):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if len(value) <= 3:
            self._age = value

# how use this

person = Person()

person.age = "20"

print(person.age)
