# ==========================================
# PYTHON OOP - ENCAPSULATION AND
# PUBLIC, PROTECTED, PRIVATE ATTRIBUTES
# ==========================================


# 1. Basic Access Modifier Example

class Student:

    def __init__(self, name, mark, cgpa):
        self.name = name          # Public attribute
        self._mark = mark         # Protected attribute
        self.__cgpa = cgpa        # Private attribute

    # Public method
    def show_info(self):
        print("Name:", self.name)
        print("Mark:", self._mark)
        print("CGPA:", self.__cgpa)

    # Getter method
    def get_cgpa(self):
        return self.__cgpa

    # Setter method
    def set_cgpa(self, new_cgpa):
        if new_cgpa >= 0 and new_cgpa <= 4:
            self.__cgpa = new_cgpa
            return "CGPA updated successfully"
        else:
            return "Invalid CGPA"


# 2. Creating Student Object

student1 = Student("Rahim", 80, 3.50)


# 3. Accessing Public Attribute

print("Public Name:", student1.name)


# 4. Accessing Protected Attribute

print("Protected Mark:", student1._mark)


# 5. Accessing Private Attribute using Method

print("Private CGPA:", student1.get_cgpa())

print("--------------------")


# 6. Updating Private Attribute

print(student1.set_cgpa(3.80))
print("Updated CGPA:", student1.get_cgpa())

print("--------------------")


# 7. Bank Account Encapsulation Example

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    # Deposit money
    def deposit(self, money):
        if money <= 0:
            return "Invalid deposit amount"

        self.__balance += money
        return "Deposit successful"

    # Withdraw money
    def withdraw(self, money):
        if money <= 0:
            return "Invalid withdraw amount"

        if money > self.__balance:
            return "Insufficient Balance"

        self.__balance -= money
        return "Withdraw successful"

    # Read private balance
    def check_balance(self):
        return self.__balance

    # Show account information
    def show_info(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.__balance)


# 8. Creating Bank Account Object

account1 = BankAccount("Junayed Islam", 1000)


# 9. Showing Initial Account

account1.show_info()

print("--------------------")


# 10. Deposit Money

print(account1.deposit(500))

print("Balance:", account1.check_balance())

print("--------------------")


# 11. Withdraw Money

print(account1.withdraw(300))

print("Balance:", account1.check_balance())

print("--------------------")


# 12. Invalid Withdraw

print(account1.withdraw(5000))

print("Final Balance:", account1.check_balance())