# ==========================================
# OOP - CLASS VS INSTANCE ATTRIBUTES
# ==========================================


# 1. Creating Class and Instance Attributes

class Student:

    university = "AIUB"
    passing_mark = 40

    def __init__(self, name, department, mark):
        self.name = name
        self.department = department
        self.mark = mark

    def show_info(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Mark:", self.mark)
        print("University:", Student.university)

    def check_result(self):
        if self.mark >= Student.passing_mark:
            return "Pass"
        else:
            return "Fail"


# 2. Creating Objects

student1 = Student("Rahim", "CSE", 80)
student2 = Student("Nadia", "BBA", 35)


# 3. Showing Object Information

print("Student 1")
student1.show_info()
print("Result:", student1.check_result())

print("--------------------")

print("Student 2")
student2.show_info()
print("Result:", student2.check_result())

print("--------------------")


# 4. Accessing Class Attribute

print("University using Class:", Student.university)
print("University using Object:", student1.university)

print("--------------------")


# 5. Changing Class Attribute

Student.university = "NSU"

print("After Changing Class Attribute")
print("Student 1 University:", student1.university)
print("Student 2 University:", student2.university)

print("--------------------")


# 6. Changing Attribute for Only One Object

student1.university = "BRAC University"

print("After Changing Only Student 1")
print("Student 1 University:", student1.university)
print("Student 2 University:", student2.university)
print("Class University:", Student.university)

print("--------------------")


# 7. Another Example

class BankAccount:

    bank_name = "ABC Bank"

    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def show_account(self):
        print("Bank:", BankAccount.bank_name)
        print("Account Holder:", self.holder_name)
        print("Balance:", self.balance)


account1 = BankAccount("Rahim", 5000)
account2 = BankAccount("Nadia", 8000)

account1.show_account()

print("--------------------")

account2.show_account()