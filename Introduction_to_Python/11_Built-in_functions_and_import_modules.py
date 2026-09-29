# ==========================================
# BUILT-IN FUNCTIONS AND IMPORT MODULES
# ==========================================


# 1. Basic Built-in Functions

name = "Rahim"
age = 22
cgpa = 3.756

print("Name:", name)
print("Length of Name:", len(name))
print("Age Type:", type(age))
print("CGPA Type:", type(cgpa))

print("--------------------")


# 2. Type Conversion

number_text = "25"

number = int(number_text)

print("Converted Number:", number)
print("Number + 5:", number + 5)

print("--------------------")


# 3. max(), min(), sum(), len()

marks = [80, 65, 95, 75, 85]

highest_mark = max(marks)
lowest_mark = min(marks)
total_marks = sum(marks)
average_mark = total_marks / len(marks)

print("Marks:", marks)
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)
print("Total Marks:", total_marks)
print("Average Mark:", average_mark)

print("--------------------")


# 4. round() and abs()

cgpa = 3.7564
difference = -15

print("Rounded CGPA:", round(cgpa, 2))
print("Absolute Value:", abs(difference))

print("--------------------")


# 5. sorted()

numbers = [40, 10, 30, 20]

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Original:", numbers)
print("Ascending:", ascending)
print("Descending:", descending)

print("--------------------")


# 6. Importing math Module

import math

number = 64

print("Square Root:", math.sqrt(number))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.9))
print("Power:", math.pow(2, 3))

print("--------------------")


# 7. Importing random Module

import random

random_number = random.randint(1, 10)
dice = random.randint(1, 6)

print("Random Number:", random_number)
print("Dice Roll:", dice)

print("--------------------")


# 8. Importing Specific Function

from math import sqrt

result = sqrt(81)

print("Square Root of 81:", result)

print("--------------------")


# 9. Using Module Alias

import math as m

print("Square Root using Alias:", m.sqrt(100))

print("--------------------")


# 10. Practical Student Example

student_marks = [78, 85, 69, 92]

total = sum(student_marks)
average = total / len(student_marks)

print("Student Marks:", student_marks)
print("Total:", total)
print("Highest:", max(student_marks))
print("Lowest:", min(student_marks))
print("Average:", round(average, 2))
print("Average Rounded Up:", math.ceil(average))