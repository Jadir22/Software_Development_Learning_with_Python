# ==========================================
# LIST, INDEX AND SLICING
# ==========================================


# 1. Creating Lists

names = ["Rahim", "Karim", "Nadia", "Sakib"]
marks = [80, 75, 90, 65]

print("Names:", names)
print("Marks:", marks)

print("--------------------")


# 2. Accessing List Items with Index

print("First Name:", names[0])
print("Second Name:", names[1])
print("Third Mark:", marks[2])

print("--------------------")


# 3. Negative Index

print("Last Name:", names[-1])
print("Second Last Name:", names[-2])

print("--------------------")


# 4. Changing a List Item

marks[1] = 85

print("Updated Marks:", marks)

print("--------------------")


# 5. List Length

print("Number of Students:", len(names))
print("Number of Marks:", len(marks))

print("--------------------")


# 6. Using index() Method

position = names.index("Nadia")

print("Index of Nadia:", position)

print("--------------------")


# 7. Basic Slicing

numbers = [10, 20, 30, 40, 50, 60]

print("Original List:", numbers)
print("Index 1 to 3:", numbers[1:4])
print("First Three:", numbers[:3])
print("From Index 2 to End:", numbers[2:])

print("--------------------")


# 8. Negative Index Slicing

print("Last Three:", numbers[-3:])
print("All Except Last:", numbers[:-1])

print("--------------------")


# 9. Slicing with Step

print("Every Second Item:", numbers[::2])
print("From Index 1 with Step 2:", numbers[1::2])

print("--------------------")


# 10. Reverse a List Using Slicing

print("Reversed List:", numbers[::-1])

print("--------------------")


# 11. Practical Student Example

students = ["Rahim", "Karim", "Nadia", "Sakib", "Mim"]

print("All Students:", students)
print("First Student:", students[0])
print("Last Student:", students[-1])
print("Middle Students:", students[1:4])
print("Index of Sakib:", students.index("Sakib"))

print("--------------------")


# 12. Marks Example

student_marks = [78, 85, 69, 92, 88]

print("All Marks:", student_marks)
print("First Mark:", student_marks[0])
print("Last Mark:", student_marks[-1])
print("First Three Marks:", student_marks[:3])
print("Last Two Marks:", student_marks[-2:])