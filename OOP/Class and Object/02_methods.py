# ==========================================
# OOP - CREATING AND USING METHODS
# ==========================================


# 1. Creating a Class with Methods

class Student:

    def show_info(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Mark:", self.mark)
        print("CGPA:", self.cgpa)

    def check_result(self):
        if self.mark >= 40:
            return "Pass"
        else:
            return "Fail"

    def update_mark(self, new_mark):
        self.mark = new_mark

    def update_cgpa(self, new_cgpa):
        self.cgpa = new_cgpa


# 2. Creating Objects

student1 = Student()
student2 = Student()


# 3. Adding Data to Student 1

student1.name = "Rahim"
student1.department = "CSE"
student1.mark = 75
student1.cgpa = 3.50


# 4. Adding Data to Student 2

student2.name = "Nadia"
student2.department = "CSE"
student2.mark = 35
student2.cgpa = 3.80


# 5. Calling Methods

print("Student 1 Information")
student1.show_info()

print("Result:", student1.check_result())

print("--------------------")

print("Student 2 Information")
student2.show_info()

print("Result:", student2.check_result())

print("--------------------")


# 6. Updating Data Using Methods

student1.update_mark(85)
student1.update_cgpa(3.75)

print("Student 1 After Update")
student1.show_info()

print("Result:", student1.check_result())

print("--------------------")


# 7. Another Simple Class with a Method

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calculator = Calculator()

print("Addition:", calculator.add(10, 20))
print("Multiplication:", calculator.multiply(5, 4))