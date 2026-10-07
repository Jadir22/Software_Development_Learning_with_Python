# ==========================================
# OOP - CONSTRUCTOR AND __init__
# ==========================================


# 1. Creating a Class with Constructor

class Student:

    def __init__(self, name, department, mark, cgpa):
        self.name = name
        self.department = department
        self.mark = mark
        self.cgpa = cgpa

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


# 2. Creating Objects with Initial Data

student1 = Student("Rahim", "CSE", 80, 3.75)
student2 = Student("Nadia", "BBA", 35, 3.80)


# 3. Showing Student 1 Information

print("Student 1 Information")

student1.show_info()

print("Result:", student1.check_result())

print("--------------------")


# 4. Showing Student 2 Information

print("Student 2 Information")

student2.show_info()

print("Result:", student2.check_result())

print("--------------------")


# 5. Updating Object Data

student2.update_mark(65)

print("Student 2 After Mark Update")

student2.show_info()

print("Result:", student2.check_result())

print("--------------------")


# 6. Another Simple Constructor Example

class Calculator:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def multiply(self):
        return self.number1 * self.number2


calculator = Calculator(10, 20)

print("Addition:", calculator.add())
print("Multiplication:", calculator.multiply())