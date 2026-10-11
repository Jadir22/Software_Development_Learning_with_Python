# ==========================================
# PYTHON OOP - MULTIPLE INHERITANCE
# ==========================================


# 1. First Parent Class

class Student:

    def __init__(self, student_id):
        self.student_id = student_id

    def study(self):
        print("Student is studying")

    def show_role(self):
        print("Role from Student class")


# 2. Second Parent Class

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print("Employee is working")

    def show_role(self):
        print("Role from Employee class")


# 3. Child Class with Multiple Inheritance

class TeachingAssistant(Student, Employee):

    def __init__(self, name, student_id, salary):
        Student.__init__(self, student_id)
        Employee.__init__(self, salary)

        self.name = name

    def assist_teacher(self):
        print(self.name, "is assisting the teacher")

    def show_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Salary:", self.salary)


# 4. Creating an Object

ta1 = TeachingAssistant(
    "Rahim",
    101,
    20000
)


# 5. Using Methods from Both Parent Classes

ta1.study()
ta1.work()

print("--------------------")


# 6. Using Child Class Method

ta1.assist_teacher()

print("--------------------")


# 7. Showing Information

ta1.show_info()

print("--------------------")


# 8. Same Method in Both Parent Classes

ta1.show_role()

print("--------------------")


# 9. Checking Method Resolution Order

print(TeachingAssistant.mro())