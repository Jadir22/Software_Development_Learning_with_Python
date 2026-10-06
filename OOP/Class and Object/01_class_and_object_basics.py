# ==========================================
# OOP - CLASS AND OBJECT BASICS
# ==========================================


# 1. Creating a Simple Class

class Student:
    pass


# 2. Creating Objects

student1 = Student()
student2 = Student()


# 3. Adding Data to Objects

student1.name = "Rahim"
student1.department = "CSE"
student1.cgpa = 3.75

student2.name = "Nadia"
student2.department = "CSE"
student2.cgpa = 3.90


# 4. Accessing Object Data

print("Student 1 Information")
print("Name:", student1.name)
print("Department:", student1.department)
print("CGPA:", student1.cgpa)

print("--------------------")

print("Student 2 Information")
print("Name:", student2.name)
print("Department:", student2.department)
print("CGPA:", student2.cgpa)

print("--------------------")


# 5. Updating Object Data

student1.cgpa = 3.80

print("Updated CGPA of Student 1:", student1.cgpa)

print("--------------------")


# 6. Checking Object Type

print("Type of student1:", type(student1))
print("Type of student2:", type(student2))

print("--------------------")


# 7. Creating Another Object

student3 = Student()

student3.name = "Karim"
student3.department = "EEE"
student3.cgpa = 3.60

print("Student 3 Information")
print("Name:", student3.name)
print("Department:", student3.department)
print("CGPA:", student3.cgpa)