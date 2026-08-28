# Basic Input, Output and Typecasting in Python

# -------------------------
# 1. Basic Input
# -------------------------

name = input("Enter your name: ")
age = input("Enter your age: ")

print()
print("Before Typecasting:")
print("Name:", name)
print("Age:", age)

print("Type of name:", type(name))
print("Type of age:", type(age))

# input() always gives string


# -------------------------
# 2. Typecasting String to Integer
# -------------------------

age = int(age)

print()
print("After converting age to int:")
print("Age:", age)
print("Type of age:", type(age))


# -------------------------
# 3. Integer Input Directly
# -------------------------

num1 = int(input("\nEnter first integer number: "))
num2 = int(input("Enter second integer number: "))

sum_value = num1 + num2

print("Sum:", sum_value)


# -------------------------
# 4. Float Input
# -------------------------

price = float(input("\nEnter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total Price:", total)


# -------------------------
# 5. Different Typecasting
# -------------------------

number = 25
decimal_number = 10.75

number_as_float = float(number)
number_as_string = str(number)
decimal_as_integer = int(decimal_number)

print()
print("Typecasting Examples:")

print("Original Integer:", number)
print("Integer to Float:", number_as_float)
print("Integer to String:", number_as_string)
print("Float to Integer:", decimal_as_integer)


# -------------------------
# 6. Check Data Types
# -------------------------

print()
print("Data Types:")

print(type(number))
print(type(number_as_float))
print(type(number_as_string))
print(type(decimal_as_integer))


# -------------------------
# 7. String vs Integer Addition
# -------------------------

text1 = "10"
text2 = "20"

print()
print("String Addition:", text1 + text2)

number1 = int(text1)
number2 = int(text2)

print("Integer Addition:", number1 + number2)


# -------------------------
# 8. int + str
# -------------------------

number = 10
text = "20"

# print(number + text)
# This gives TypeError because int and str cannot be added directly

print()
print("Convert text to int:", number + int(text))
print("Convert number to str:", str(number) + text)


# -------------------------
# 9. Final User Information
# -------------------------

student_name = input("\nEnter student name: ")
student_age = int(input("Enter student age: "))
student_cgpa = float(input("Enter student CGPA: "))

print()
print("Student Information")
print("Name:", student_name)
print("Age:", student_age)
print("CGPA:", student_cgpa)

print()
print("Student Data Types:")
print("Name:", type(student_name))
print("Age:", type(student_age))
print("CGPA:", type(student_cgpa))