# ==========================================
# LOCAL AND GLOBAL SCOPE
# ==========================================


# 1. Global Variable

university = "AIUB"

print("Global University:", university)

print("--------------------")


# 2. Accessing Global Variable Inside Function

def show_university():
    print("Inside Function:", university)


show_university()

print("--------------------")


# 3. Local Variable

def student_info():
    name = "Rahim"
    age = 22

    print("Name:", name)
    print("Age:", age)


student_info()

print("--------------------")


# 4. Same Variable Name in Local and Global Scope

name = "Karim"

def show_name():
    name = "Nadia"
    print("Local Name:", name)


show_name()

print("Global Name:", name)

print("--------------------")


# 5. Changing Global Variable with global Keyword

score = 50

def update_score():
    global score
    score = score + 10


update_score()

print("Updated Global Score:", score)

print("--------------------")


# 6. Function Parameters are Local

def show_result(student_name, marks):
    if marks >= 40:
        status = "Pass"
    else:
        status = "Fail"

    print("Student:", student_name)
    print("Marks:", marks)
    print("Status:", status)


show_result("Sakib", 75)

print("--------------------")


# 7. Local Variables in Different Functions

def first_function():
    number = 10
    print("First Function:", number)


def second_function():
    number = 20
    print("Second Function:", number)


first_function()
second_function()

print("--------------------")


# 8. Better Alternative to Changing Global Variable

def increase_marks(current_marks):
    new_marks = current_marks + 5
    return new_marks


marks = 70
marks = increase_marks(marks)

print("New Marks:", marks)

print("--------------------")


# 9. Practical Example

college = "AIUB"

def student_result(name, marks):
    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("University:", college)
    print("Student:", name)
    print("Marks:", marks)
    print("Result:", result)


student_result("Nadia", 85)