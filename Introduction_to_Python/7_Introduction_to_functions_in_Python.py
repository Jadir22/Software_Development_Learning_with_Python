# Introduction to Functions in Python


# 1. Simple Function

def greet():
    print("Hello, Welcome to Python!")

greet()

print()


# 2. Function with Parameter

def greet_user(name):
    print("Hello", name)

greet_user("Rahim")
greet_user("Karim")

print()


# 3. Function with Multiple Parameters

def add(a, b):
    print("Sum:", a + b)

add(10, 20)

print()


# 4. Function with User Input

def subtract(a, b):
    print("Subtraction:", a - b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

subtract(num1, num2)

print()


# 5. Function with Return

def multiply(a, b):
    return a * b

result = multiply(5, 4)

print("Multiplication:", result)

print()


# 6. Using Returned Value Again

final_result = result + 10

print("After adding 10:", final_result)

print()


# 7. Function with Condition

def check_even_odd(number):

    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

number = int(input("Enter a number: "))

check_even_odd(number)

print()


# 8. Function with if-elif-else

def check_number(number):

    if number > 0:
        print("Positive Number")

    elif number < 0:
        print("Negative Number")

    else:
        print("Zero")

number = int(input("Enter another number: "))

check_number(number)

print()


# 9. Function with Loop

def print_numbers():

    for i in range(1, 6):
        print(i)

print("Numbers from 1 to 5:")
print_numbers()

print()


# 10. Function with Parameter, Loop and Calculation

def multiplication_table(number):

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

number = int(input("Enter number for multiplication table: "))

multiplication_table(number)