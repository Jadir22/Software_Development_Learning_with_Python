# ==========================================
# LIST METHODS IN PYTHON
# ==========================================


# 1. append()

marks = [70, 80, 90]

marks.append(85)

print("After append:", marks)

print("--------------------")


# 2. insert()

names = ["Rahim", "Karim", "Nadia"]

names.insert(1, "Sakib")

print("After insert:", names)

print("--------------------")


# 3. extend()

marks = [70, 80]

new_marks = [90, 85]

marks.extend(new_marks)

print("After extend:", marks)

print("--------------------")


# 4. remove()

students = ["Rahim", "Karim", "Nadia"]

students.remove("Karim")

print("After remove:", students)

print("--------------------")


# 5. pop()

students = ["Rahim", "Karim", "Nadia"]

removed_student = students.pop()

print("After pop:", students)
print("Removed Student:", removed_student)

print("--------------------")


# 6. pop() with Index

students = ["Rahim", "Karim", "Nadia"]

removed_student = students.pop(1)

print("After pop(1):", students)
print("Removed Student:", removed_student)

print("--------------------")


# 7. index()

names = ["Rahim", "Karim", "Nadia", "Sakib"]

position = names.index("Nadia")

print("Index of Nadia:", position)

print("--------------------")


# 8. count()

results = ["Pass", "Fail", "Pass", "Pass", "Fail"]

print("Pass Count:", results.count("Pass"))
print("Fail Count:", results.count("Fail"))

print("--------------------")


# 9. sort()

marks = [80, 65, 95, 70, 85]

marks.sort()

print("Ascending:", marks)

marks.sort(reverse=True)

print("Descending:", marks)

print("--------------------")


# 10. reverse()

numbers = [10, 20, 30, 40]

numbers.reverse()

print("Reversed:", numbers)

print("--------------------")


# 11. copy()

original_marks = [70, 80, 90]

copied_marks = original_marks.copy()

copied_marks.append(100)

print("Original Marks:", original_marks)
print("Copied Marks:", copied_marks)

print("--------------------")


# 12. clear()

temporary_list = [1, 2, 3, 4]

temporary_list.clear()

print("After clear:", temporary_list)

print("--------------------")


# 13. Practical Student Marks Example

student_marks = [75, 80, 65, 90]

print("Original Marks:", student_marks)

# Add a new mark
student_marks.append(85)

# Add a mark at a specific position
student_marks.insert(1, 88)

# Remove a wrong mark
student_marks.remove(65)

# Sort marks from highest to lowest
student_marks.sort(reverse=True)

print("Updated Marks:", student_marks)
print("Highest Mark:", student_marks[0])
print("Number of 80 Marks:", student_marks.count(80))