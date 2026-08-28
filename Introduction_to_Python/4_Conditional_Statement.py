# Conditional Statements in Python

# --------------------------------
# 1. Basic if
# --------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")

print()


# --------------------------------
# 2. if-else
# --------------------------------

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print()


# --------------------------------
# 3. if-elif-else
# --------------------------------

number = int(input("Enter another number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

print()


# --------------------------------
# 4. Grade Checking
# --------------------------------

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Fail")

print()


# --------------------------------
# 5. Using and
# --------------------------------

age = int(input("Enter age for eligibility: "))
cgpa = float(input("Enter CGPA: "))

if age >= 18 and cgpa >= 3.00:
    print("Eligible")
else:
    print("Not Eligible")

print()


# --------------------------------
# 6. Using or
# --------------------------------

day = input("Enter day: ")

if day == "Friday" or day == "Saturday":
    print("Weekend")
else:
    print("Working Day")

print()


# --------------------------------
# 7. Using not
# --------------------------------

is_raining = False

if not is_raining:
    print("You can go outside")
else:
    print("Take an umbrella")

print()


# --------------------------------
# 8. String Comparison
# --------------------------------

name = input("Enter your name: ")

if name == "Rahim":
    print("Welcome Rahim")
else:
    print("Welcome Guest")

print()


# --------------------------------
# 9. Case-insensitive Comparison
# --------------------------------

answer = input("Do you want to continue? ")

if answer.lower() == "yes":
    print("Continuing...")
else:
    print("Stopped")

print()


# --------------------------------
# 10. Nested if
# --------------------------------

username = input("Enter username: ")

if username == "admin":
    password = input("Enter password: ")

    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")

print()


# --------------------------------
# 11. Another Nested if Example
# --------------------------------

age = int(input("Enter your age again: "))

if age >= 18:
    print("You are an adult")

    if age >= 60:
        print("You are also a senior citizen")
else:
    print("You are under 18")