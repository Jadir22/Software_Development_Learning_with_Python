# ==========================================
# OOP - BANK ACCOUNT
# ==========================================


class BankAccount:

    # 1. Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # 2. Deposit Money
    def deposit(self, money):
        if money <= 0:
            return "Invalid deposit amount"

        self.balance = self.balance + money
        return self.balance

    # 3. Withdraw Money
    def withdraw(self, money):
        if money <= 0:
            return "Invalid withdraw amount"

        if money > self.balance:
            return "Insufficient Balance"

        self.balance = self.balance - money
        return self.balance

    # 4. Check Current Balance
    def check_balance(self):
        return self.balance

    # 5. Show Account Information
    def show_info(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


# 6. Creating an Object

acc1 = BankAccount("Junayed Islam", 500)


# 7. Showing Initial Account Information

print("Initial Account Information")
acc1.show_info()

print("--------------------")


# 8. Withdraw Money

withdraw_result = acc1.withdraw(300)

print("After Withdraw:", withdraw_result)

print("--------------------")


# 9. Deposit Money

deposit_result = acc1.deposit(1000)

print("After Deposit:", deposit_result)

print("--------------------")


# 10. Check Final Balance

print("Final Balance:", acc1.check_balance())

print("--------------------")


# 11. Testing Insufficient Balance

print("Withdraw 2000:", acc1.withdraw(2000))

print("--------------------")


# 12. Final Account Information

print("Final Account Information")
acc1.show_info()