# ==========================================
# PYTHON - INNER AND WRAPPER FUNCTIONS
# ==========================================


# 1. Basic Inner Function

def outer_function():

    def inner_function():
        print("Hello from inner function")

    inner_function()


outer_function()

print("--------------------")


# 2. Inner Function Using Outer Variable

def show_student():

    name = "Rahim"

    def show_name():
        print("Student Name:", name)

    show_name()


show_student()

print("--------------------")


# 3. Inner Function with Calculation

def calculate_square(number):

    def square():
        return number * number

    return square()


print("Square:", calculate_square(5))

print("--------------------")


# 4. Returning an Inner Function

def create_greeting():

    def greet():
        print("Hello Python")

    return greet


greeting_function = create_greeting()

greeting_function()

print("--------------------")


# 5. Function as an Argument

def say_hello():
    print("Hello")


def execute_function(func):
    func()


execute_function(say_hello)

print("--------------------")


# 6. Basic Wrapper Function

def greet():
    print("Hello Rahim")


def wrapper(func):

    def inner():
        print("Before function")

        func()

        print("After function")

    return inner


new_greet = wrapper(greet)

new_greet()

print("--------------------")


# 7. Wrapper with Parameters

def add(a, b):
    return a + b


def calculation_wrapper(func):

    def inner(a, b):
        print("Calculation started")

        result = func(a, b)

        print("Calculation finished")

        return result

    return inner


new_add = calculation_wrapper(add)

answer = new_add(10, 20)

print("Result:", answer)

print("--------------------")


# 8. Practical Login Wrapper Example

def login():
    print("User logged in successfully")


def security_wrapper(func):

    def inner():
        print("Checking permission...")

        func()

        print("Action completed")

    return inner


secured_login = security_wrapper(login)

secured_login()