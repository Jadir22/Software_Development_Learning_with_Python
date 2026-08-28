# Basic Operators and Comparison in Python

# --------------------------------
# 1. Taking Input
# --------------------------------

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print()


# --------------------------------
# 2. Arithmetic Operators
# --------------------------------

print("Arithmetic Operators")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

print()


# --------------------------------
# 3. Comparison Operators
# --------------------------------

print("Comparison Operators")

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print()


# --------------------------------
# 4. Assignment Operators
# --------------------------------

print("Assignment Operators")

x = 10
print("Initial x:", x)

x += 5
print("After x += 5:", x)

x -= 3
print("After x -= 3:", x)

x *= 2
print("After x *= 2:", x)

x /= 4
print("After x /= 4:", x)

print()


# --------------------------------
# 5. More Assignment Operators
# --------------------------------

y = 10

y //= 3
print("After y //= 3:", y)

z = 10

z %= 3
print("After z %= 3:", z)

p = 2

p **= 3
print("After p **= 3:", p)

print()


# --------------------------------
# 6. Logical Operators
# --------------------------------

age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))

print()

print("Logical Operators")

print("Age >= 18:", age >= 18)
print("CGPA >= 3.00:", cgpa >= 3.00)

print("AND:", age >= 18 and cgpa >= 3.00)
print("OR:", age >= 18 or cgpa >= 3.00)
print("NOT:", not age >= 18)

print()


# --------------------------------
# 7. Boolean Example
# --------------------------------

is_student = True

print("is_student:", is_student)
print("not is_student:", not is_student)

print()


# --------------------------------
# 8. String Comparison
# --------------------------------

name = input("Enter your name: ")

print("Is your name Rahim?:", name == "Rahim")
print("Is your name not Rahim?:", name != "Rahim")

print()


# --------------------------------
# 9. Operator Precedence
# --------------------------------

result1 = 10 + 5 * 2
result2 = (10 + 5) * 2

print("Without Parentheses:", result1)
print("With Parentheses:", result2)

print()


# --------------------------------
# 10. Even or Odd Logic Using %
# --------------------------------

number = int(input("Enter a number to check remainder: "))

print("Remainder after dividing by 2:", number % 2)
print("Is Even:", number % 2 == 0)
print("Is Odd:", number % 2 != 0)