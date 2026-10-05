# ==========================================
# TRY, EXCEPT, FINALLY AND FILE HANDLING
# ==========================================


# 1. Basic Try-Except

try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Invalid age. Please enter numbers only.")

print("--------------------")


# 2. Handling Multiple Exceptions

try:
    number = int(input("Enter a number to divide 100: "))
    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Calculation finished.")

print("--------------------")


# 3. Writing Data to a File

name = input("Enter student name: ")
department = input("Enter department: ")
mark = input("Enter mark: ")

with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Department: " + department + "\n")
    file.write("Mark: " + mark + "\n")

print("Student information saved.")

print("--------------------")


# 4. Appending New Data

with open("student.txt", "a") as file:
    file.write("Status: Active\n")

print("New information added.")

print("--------------------")


# 5. Reading the File

try:
    with open("student.txt", "r") as file:
        content = file.read()

    print("Student Information:")
    print(content)

except FileNotFoundError:
    print("Student file was not found.")

finally:
    print("File reading operation finished.")

print("--------------------")


# 6. Practical Result Example

try:
    mark = int(input("Enter student mark: "))

    if mark >= 40:
        status = "Pass"
    else:
        status = "Fail"

    with open("result.txt", "w") as file:
        file.write("Mark: " + str(mark) + "\n")
        file.write("Result: " + status + "\n")

    print("Result saved successfully.")

except ValueError:
    print("Invalid mark. Please enter a number.")

finally:
    print("Program finished.")