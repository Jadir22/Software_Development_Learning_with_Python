# ==========================================
# DEFAULT PARAMETERS AND *ARGS
# ==========================================


# 1. Basic Default Parameter

def greet(name="Guest"):
    print("Hello,", name)


greet()
greet("Rahim")

print("--------------------")


# 2. Multiple Default Parameters

def student_info(name, age=20, department="CSE"):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)


student_info("Nadia")
print()

student_info("Karim", 22, "BBA")

print("--------------------")


# 3. Using Keyword Arguments

def show_result(name, cgpa=3.50, semester=1):
    print("Name:", name)
    print("CGPA:", cgpa)
    print("Semester:", semester)


show_result("Sakib", cgpa=3.80)

print("--------------------")


# 4. Basic *args Example

def show_numbers(*args):
    print("All numbers:", args)

    for number in args:
        print(number)


show_numbers(10, 20, 30, 40)

print("--------------------")


# 5. Sum Using *args

def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    print("Total:", total)


add_numbers(10, 20)
add_numbers(10, 20, 30, 40)

print("--------------------")


# 6. Normal Parameter with *args

def student_marks(name, *marks):
    print("Student:", name)
    print("Marks:", marks)

    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    print("Average Mark:", average)


student_marks("Rahim", 80, 90, 70)

print("--------------------")


# 7. Default Parameter with *args

def check_marks(name, *marks, passing_mark=40):
    print("Student:", name)
    print("Passing Mark:", passing_mark)

    for mark in marks:
        if mark >= passing_mark:
            print(mark, "- Pass")
        else:
            print(mark, "- Fail")


check_marks("Nadia", 75, 35, 60)

print()

check_marks("Karim", 70, 45, 55, passing_mark=50)