# ==========================================
# PYTHON OOP - PROPERTY, GETTER, SETTER
# AND READ-ONLY PROPERTY
# ==========================================

# 1. Student Class

class Student:

    def __init__(self, student_id, name, mark):
        self.__student_id = student_id
        self.name = name
        self.__mark = mark

    # 2. Read-only Property
    @property
    def student_id(self):
        return self.__student_id

    # 3. Getter Property
    @property
    def mark(self):
        return self.__mark

    # 4. Setter Property
    @mark.setter
    def mark(self, new_mark):
        if new_mark >= 0 and new_mark <= 100:
            self.__mark = new_mark
        else:
            print("Invalid mark")

    # 5. Show Student Information
    def show_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Mark:", self.mark)


# 6. Creating Student Object

student1 = Student(101, "Rahim", 80)


# 7. Reading Properties

print("Student ID:", student1.student_id)
print("Mark:", student1.mark)

print("--------------------")


# 8. Updating Mark using Setter

student1.mark = 95

print("Updated Mark:", student1.mark)

print("--------------------")


# 9. Testing Invalid Mark

student1.mark = 150

print("Current Mark:", student1.mark)

print("--------------------")


# 10. Showing Full Information

student1.show_info()

print("--------------------")


# 11. Bank Account Example

class BankAccount:

    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance

    # Read-only Account Number
    @property
    def account_number(self):
        return self.__account_number

    # Balance Getter
    @property
    def balance(self):
        return self.__balance

    # Balance Setter
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative")


account1 = BankAccount("ACC-101", "Jadir", 5000)

print("Account Number:", account1.account_number)
print("Initial Balance:", account1.balance)

account1.balance = 7000

print("Updated Balance:", account1.balance)

# This would cause an error because
# account_number is read-only:
# account1.account_number = "ACC-999"