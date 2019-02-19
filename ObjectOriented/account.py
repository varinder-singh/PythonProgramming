import datetime
import pytz


class Account:

    """This is an example of encapsulation, inheritance and composition.
    This class also implements the static method in python"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [("Deposit", Account._current_time(), balance)]

    def show_account_summary(self):
        print("Account Name : {} and balance in the account is {}".format(self.name, self.balance))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount of {} deposited successfully. New balance in the account is {}".format(amount, self.balance))
            self.transaction_list.append(('Deposit', Account._current_time(), amount))
        else:
            print("Please enter an amount greater than 0")

    def withdraw(self, amount):
        if amount < self.balance > 0:
            self.balance -= amount
            print("Amount of {} deposited successfully. New balance in the account is {}".format(amount, self.balance))
            self.transaction_list.append(('Withdrawal', Account._current_time(), amount))
        else:
            print("""Please enter an amount greater than 0 
            or an amount less than the account total withdrawal balance : {}""".format(self.balance))

    def show_transaction(self):
        for t_type, date, amount in self.transaction_list:
            print("Transaction type :{} for an amount of :{} happened on :{}".format(t_type,amount,date))


if __name__ == '__main__':
    name = input("Enter the name of the person for which the account to be opened : ")
    ac = Account(name, 1000)
    ac.show_account_summary()
    amount_deposit = int(input("enter the amount to be deposited : "))
    ac.deposit(amount_deposit)
    amount_withdraw = int(input("enter the amount to be withdrawn : "))
    ac.withdraw(amount_withdraw)

    ac.show_transaction()
