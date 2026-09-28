# ==========================================
# **KWARGS AND MULTIPLE RETURN VALUES
# ==========================================


# 1. Basic **kwargs Example

def show_info(**kwargs):
    print(kwargs)


show_info(name="Rahim", age=22, department="CSE")

print("--------------------")


# 2. Accessing Values from **kwargs

def student_info(**kwargs):
    print("Name:", kwargs["name"])
    print("Department:", kwargs["department"])


student_info(name="Nadia", department="CSE")

print("--------------------")


# 3. Looping Through **kwargs

def show_student_details(**kwargs):
    for key in kwargs:
        print(key, ":", kwargs[key])


show_student_details(
    name="Karim",
    age=21,
    cgpa=3.80,
    department="CSE"
)

print("--------------------")


# 4. Normal Parameter with **kwargs

def student(name, **kwargs):
    print("Student Name:", name)

    for key in kwargs:
        print(key, ":", kwargs[key])


student(
    "Rahim",
    age=22,
    department="CSE",
    semester=10
)

print("--------------------")


# 5. Using *args and **kwargs Together

def student_result(name, *marks, **info):
    print("Name:", name)
    print("Marks:", marks)

    total = 0

    for mark in marks:
        total += mark

    print("Total Marks:", total)

    for key in info:
        print(key, ":", info[key])


student_result(
    "Nadia",
    80,
    90,
    70,
    department="CSE",
    semester=10
)

print("--------------------")


# 6. Basic Multiple Return

def calculate(a, b):
    total = a + b
    difference = a - b

    return total, difference


sum_result, difference_result = calculate(20, 10)

print("Sum:", sum_result)
print("Difference:", difference_result)

print("--------------------")


# 7. Practical Multiple Return Example

def calculate_marks(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3

    if average >= 40:
        status = "Pass"
    else:
        status = "Fail"

    return total, average, status


total, average, status = calculate_marks(80, 70, 60)

print("Total:", total)
print("Average:", average)
print("Status:", status)

print("--------------------")


# 8. **kwargs with Multiple Return

def student_summary(name, *marks, **info):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    if average >= 40:
        status = "Pass"
    else:
        status = "Fail"

    print("Name:", name)

    for key in info:
        print(key, ":", info[key])

    return total, average, status


total, average, status = student_summary(
    "Sakib",
    75,
    85,
    65,
    department="CSE",
    semester=10
)

print("Total Marks:", total)
print("Average Mark:", average)
print("Status:", status)