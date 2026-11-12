
# * instance attribute
# ? بیرون از کلاس تعریف میشود و فقط مختص یک obj هست
# *‌ class attribute
# ? داخل کلاس و با self تعریف میشود


from random import randrange
from typing import Set, List


class BankAccount:

    all_account_numbers: List[int] = []
    last_account_number = 99

    def __init__(self, first_name:str, last_name:str="") -> None:
        self.firstname = first_name
        self.lastname = last_name
        self.balance = 0
        BankAccount.last_account_number += 1
        AC_NU = BankAccount.last_account_number
        self.account_number:float = AC_NU
        BankAccount.all_account_numbers.append(AC_NU)

    def display(self) -> None:
        """Display the account details of the bank account.

        Returns:
            str: Formatted string containing account holder's name and current balance.
        """
        return f"{"*"*40}\nHi, {self.firstname} {self.lastname}\n Your cuosirrent balance: {self.balance}\n{"*"*40}"

    def deposit(self) -> None:
        """_summary_

        Returns:
            _type_: _description_
        """
        amount = float(input("Please enter amount to deposit: "))
        self.balance += amount
        return self.display()

    def withdraw(self) -> None:
        amount = float(input("Please enter amount to withdraw: "))
        if amount > self.balance:
            return "Insufficient Balance!"
        else:
            self.balance -= amount
            return self.display()


a = BankAccount("amir")
a.x = 12 #!  instance attribute
print(dir(a), "*"*45) # ['account_number', 'all_account_numbers', 'balance', 
# 'deposit', 'display', 'firstname', 'last_account_number', 'lastname', 'withdraw', 'x']

b = BankAccount("ali")
print(dir(a), "*"*45) # not how x in attr 

# ! مثال مهم و قابل استفاده

# TODO class
#from __future__ import annotations

from pprint import pprint

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

ob_1 = User("amir", "amir@gmail.com", "1234")
ob_1.all_user = [] # ارجیت نصبت به all user in class
ob_2 = User("ali", "ali@gmail.com", "1646")
ob_3 = User("attila", "attila@gmail.com", "1646")
print(str(ob_1))
print(repr(ob_1))
print(dir(ob_1))
pprint(User.all_user)
pprint(ob_1.all_user)
