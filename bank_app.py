

class Customer:
    def __init__(self, last_name, first_name, username, password, account_number):
        self.last_name = last_name
        self.first_name = first_name
        self.username = username
        self.password = password
        self.account_number = account_number


class Account:
    def __init__(self, balance, deposit, withdraw, transfer, statement, transactions):
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw
        self.transfer = transfer
        self.statement = statement
        self.transactions = transactions

    def balance(self, balance):
        return self.balance

    def deposit(self, deposit):
        pass

    def transfer(self, transfer):
        pass

    def statement(self, statement):
        pass

    def transactions(self, transactions):
        pass


class Savings_Account(Account):
    def __init__(self, balance, deposit, transfer, statement, transactions, interest):
        super().__init__(balance, deposit, transfer, statement, transactions)
        self.interest = interest
    pass


class Transaction:
    def __init__(self, deposit, withdrawal, transfer):
        pass


class Bank:
    pass


def main():
    print("Welcome to the Bank")

    main_menu = input("How can we be of service?\n 1. Register New Account\n 2. Login\n 3. Exit\n")
    if main_menu == "1":
        # get customer information
        last_name = input("Please enter you last name: ")
        first_name = input("Please enter your first name: ")
        username = input("Enter username: ")
        password = input("Enter a password: ")

    elif main_menu == "2":
        pass

    elif main_menu == "3":
        pass

    else:
        print("Invalid entry, please try again.")


main()