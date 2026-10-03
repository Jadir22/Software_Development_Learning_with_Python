# ==========================================
# TUPLES AND TUPLE METHODS IN PYTHON
# ==========================================


# 1. Creating a Tuple

students = ("Rahim", "Karim", "Nadia")

print("Students:", students)

print("--------------------")


# 2. Accessing Items with Index

print("First Student:", students[0])
print("Second Student:", students[1])
print("Last Student:", students[-1])

print("--------------------")


# 3. Tuple Slicing

numbers = (10, 20, 30, 40, 50)

print("Original Tuple:", numbers)
print("Index 1 to 3:", numbers[1:4])
print("First Three:", numbers[:3])
print("From Index 2:", numbers[2:])

print("--------------------")


# 4. Single Item Tuple

single_number = (10,)

print("Single Item Tuple:", single_number)
print("Type:", type(single_number))

print("--------------------")


# 5. Tuple Length

marks = (80, 70, 90, 85)

print("Marks:", marks)
print("Number of Marks:", len(marks))

print("--------------------")


# 6. count() Method

marks = (80, 70, 80, 90, 80)

print("Number of 80 Marks:", marks.count(80))

print("--------------------")


# 7. index() Method

names = ("Rahim", "Karim", "Nadia", "Sakib")

print("Index of Nadia:", names.index("Nadia"))

print("--------------------")


# 8. Using in with Tuple

subjects = ("Python", "Java", "C++")

if "Python" in subjects:
    print("Python was found")

if "C#" not in subjects:
    print("C# was not found")

print("--------------------")


# 9. Looping Through a Tuple

for subject in subjects:
    print(subject)

print("--------------------")


# 10. Tuple Packing

student = ("Rahim", 22, 3.75)

print("Student Tuple:", student)

print("--------------------")


# 11. Tuple Unpacking

name, age, cgpa = student

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)

print("--------------------")


# 12. Tuple is Immutable

marks = (70, 80, 90)

# marks[0] = 75   # This would cause an error

print("Tuple cannot be changed directly:", marks)

print("--------------------")


# 13. Converting Tuple to List to Modify It

marks = (70, 80, 90)

marks_list = list(marks)

marks_list[0] = 75
marks_list.append(95)

marks = tuple(marks_list)

print("Modified Tuple:", marks)

print("--------------------")


# 14. Practical Result Example

results = ("Pass", "Fail", "Pass", "Pass", "Fail")

print("All Results:", results)
print("Passed Students:", results.count("Pass"))
print("Failed Students:", results.count("Fail"))
print("First Fail Index:", results.index("Fail"))