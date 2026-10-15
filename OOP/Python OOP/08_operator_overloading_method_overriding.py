# ==========================================
# PYTHON OOP - OPERATOR OVERLOADING
# AND METHOD OVERRIDING
# ==========================================


# 1. Method Overriding

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog says Bark")


class Cat(Animal):

    def sound(self):
        print("Cat says Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

print("--------------------")


# 2. Operator Overloading with +

class Student:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __add__(self, other):
        return self.mark + other.mark

    def __eq__(self, other):
        return self.mark == other.mark

    def __gt__(self, other):
        return self.mark > other.mark


student1 = Student("Rahim", 80)
student2 = Student("Junayed", 90)
student3 = Student("Fahim", 80)


# 3. Using + Operator

total_marks = student1 + student2

print("Total Marks:", total_marks)

print("--------------------")


# 4. Using == Operator

print("Student 1 and Student 3 have same mark:")
print(student1 == student3)

print("--------------------")


# 5. Using > Operator

print("Does Student 1 have more marks than Student 2?")
print(student1 > student2)

print("--------------------")


# 6. Practical Bank Account Example

class BankAccount:

    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

    def __gt__(self, other):
        return self.balance > other.balance


account1 = BankAccount("Rahim", 5000)
account2 = BankAccount("Junayed", 8000)

print("Combined Balance:", account1 + account2)

print("Does Account 1 have more balance than Account 2?", account1 > account2)