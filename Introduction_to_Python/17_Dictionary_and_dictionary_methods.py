# ==========================================
# DICTIONARY AND DICTIONARY METHODS
# ==========================================


# 1. Creating a Dictionary

student = {
    "name": "Rahim",
    "age": 22,
    "department": "CSE",
    "cgpa": 3.75
}

print("Student:", student)

print("--------------------")


# 2. Accessing Values

print("Name:", student["name"])
print("Age:", student["age"])
print("Department:", student["department"])

print("--------------------")


# 3. Using get()

print("CGPA:", student.get("cgpa"))
print("Semester:", student.get("semester", "Not Found"))

print("--------------------")


# 4. Changing a Value

student["cgpa"] = 3.85

print("Updated CGPA:", student["cgpa"])

print("--------------------")


# 5. Adding a New Key-Value Pair

student["semester"] = 10

print("After Adding Semester:", student)

print("--------------------")


# 6. keys(), values(), items()

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("--------------------")


# 7. Looping Through Dictionary

for key, value in student.items():
    print(key, ":", value)

print("--------------------")


# 8. update()

student.update({
    "age": 23,
    "university": "AIUB"
})

print("After Update:", student)

print("--------------------")


# 9. Checking a Key

if "cgpa" in student:
    print("CGPA Found:", student["cgpa"])
else:
    print("CGPA Not Found")

print("--------------------")


# 10. pop()

removed_age = student.pop("age")

print("Removed Age:", removed_age)
print("After pop:", student)

print("--------------------")


# 11. copy()

student_copy = student.copy()

student_copy["name"] = "Karim"

print("Original Student:", student)
print("Copied Student:", student_copy)

print("--------------------")


# 12. Nested Dictionary

student_result = {
    "name": "Nadia",
    "marks": {
        "Python": 85,
        "Java": 75,
        "C++": 90
    }
}

print("Student Name:", student_result["name"])
print("Python Mark:", student_result["marks"]["Python"])
print("Java Mark:", student_result["marks"]["Java"])

print("--------------------")


# 13. List of Dictionaries

students = [
    {"name": "Rahim", "mark": 80},
    {"name": "Karim", "mark": 35},
    {"name": "Nadia", "mark": 90}
]

for item in students:
    if item["mark"] >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(
        "Name:", item["name"],
        "| Mark:", item["mark"],
        "| Result:", result
    )

print("--------------------")


# 14. Practical Dictionary Example

result = {
    "name": "Sakib",
    "mark": 78
}

if result["mark"] >= 40:
    result["status"] = "Pass"
else:
    result["status"] = "Fail"

print("Final Result:", result)

print("--------------------")


# 15. clear()

temporary_data = {
    "a": 1,
    "b": 2
}

temporary_data.clear()

print("After Clear:", temporary_data)