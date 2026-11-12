from random import randrange
from typing import Set, List


class BankAccount:
    """BankAccount class to manage individual bank accounts.

    Attributes:
        firstname (str): First name of the account holder.
        lastname (str): Last name of the account holder.
        balance (float): Current balance of the account.
        account_number (float): Unique account number assigned to the account.

    Class Attributes:
        all_account_numbers (List[int]): List of all assigned account numbers.
        last_account_number (int): Last assigned account number.

    Returns:
        _type_: _description_

    Returns:
        _type_: _description_
    """
    #all_account_numbers: Set[int] = set()
    # ? نکته : attr های خارج از متود بدون سلف هست
    # نسخه بهینه تر برای سرعت به جای random
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
        # حلقه پایین برای روش غیر بهینه هست
        # self.account_number:float = 0
        # while True:
        #     if (Ac_Nu := randrange(100, 1000)) not in self.all_account_numbers:
        #         BankAccount.all_account_numbers.add(Ac_Nu)
        #         self.account_number = Ac_Nu
        #         break

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

# account_one = BankAccount("ali")
# account_two = BankAccount("amir")

# print(account_one.display())
# print(account_two.display())

# print(account_one.account_number)
# print(account_two.account_number)

# print(account_two.deposit())

# print(account_two.withdraw())

def main_bank_account():
    """Main function to interact with the bank account.

    This function creates a bank account for the user and provides a menu
    to check balance, deposit, withdraw, or exit the account.

    Returns:
        None
    """
    account_three = BankAccount("Amir", "Rikhtegarzadeh")
    print("*"*30 ,"\n" ,"wellcome",account_three.firstname, account_three.lastname)
    print(f"your balance account: {account_three.balance}")
    print(f"account number: {account_three.account_number}")
    print("_"*45)
    
    while True:
        chack = int(input("Enter your choice:\n(1 = see balance)\n(2 = see deposit)\n(3 = withdraw)\n(4 = Cansel or End)\n>>>"))    
        if chack == 1:
            print(account_three.display())
        elif chack == 2:
            print(account_three.deposit())
        elif chack == 3:
            print(account_three.withdraw())
        elif chack == 4:
            print("close your account")
            break
        else:
            print("!your choice not true!")
            print("!Please enter a true valid number.!")

if __name__ == "__main__":
    main_bank_account()


# دوتا نکته
# from typing import Set
# all_account_numbers: Set[int] = set()
# نکته : attr های خارج از متود بدون سلف هست

print("تست روش بهینه")
obj = BankAccount("ali")
print(obj.account_number)
