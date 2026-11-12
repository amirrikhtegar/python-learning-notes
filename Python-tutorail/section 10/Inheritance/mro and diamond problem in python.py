
# * MRO and Diamond 
#!___________________________________!


#? مثال ساده

class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("calling Base")
        self.num_base_calls += 1

class LftSubClass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("calling Left")
        self.num_left_calls += 1

class RightSubClass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("calling Right")
        self.num_right_calls += 1


class SubClass(LftSubClass, RightSubClass):
    num_sub_calls = 0

    def call_me(self):
        LftSubClass.call_me(self)
        RightSubClass.call_me(self)
        print("calling Sub")
        self.num_sub_calls += 1



ob = SubClass()
ob.call_me()

#* MRO
# برای حل مشکل دوبار فراخوانی base_class
print("*"*40)

class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("calling Base")
        self.num_base_calls += 1

class LftSubClass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me()
        print("calling Left")
        self.num_left_calls += 1

class RightSubClass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("calling Right")
        self.num_right_calls += 1


class SubClass(LftSubClass, RightSubClass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()

        print("calling Sub")
        self.num_sub_calls += 1



ob1 = SubClass()
ob1.call_me()

from pprint import pprint

pprint(SubClass.__mro__)