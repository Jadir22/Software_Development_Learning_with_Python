# While Loop in Python

# --------------------------------
# 1. Basic While Loop
# --------------------------------

i = 1

while i <= 5:
    print(i)
    i += 1

print()


# --------------------------------
# 2. Reverse Counting
# --------------------------------

i = 5

while i >= 1:
    print(i)
    i -= 1

print()


# --------------------------------
# 3. Even Numbers
# --------------------------------

i = 1

while i <= 10:
    if i % 2 == 0:
        print(i)

    i += 1

print()


# --------------------------------
# 4. Odd Numbers
# --------------------------------

i = 1

while i <= 10:
    if i % 2 != 0:
        print(i)

    i += 1

print()


# --------------------------------
# 5. Sum Using While Loop
# --------------------------------

i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print("Total:", total)

print()


# --------------------------------
# 6. Multiplication Table
# --------------------------------

number = int(input("Enter a number for multiplication table: "))

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1

print()


# --------------------------------
# 7. Condition-Based While Loop
# --------------------------------

number = int(input("Enter a positive number: "))

while number > 0:
    print("You entered:", number)
    number = int(input("Enter another positive number: "))

print("Positive number loop ended")

print()


# --------------------------------
# 8. Password Checking
# --------------------------------

password = input("Enter password: ")

while password != "1234":
    print("Wrong Password")
    password = input("Enter password again: ")

print("Login Successful")

print()


# --------------------------------
# 9. break
# --------------------------------

i = 1

while i <= 10:
    print(i)

    if i == 5:
        break

    i += 1

print("Loop stopped using break")

print()


# --------------------------------
# 10. continue
# --------------------------------

i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)

print()


# --------------------------------
# 11. while True
# --------------------------------

while True:
    number = int(input("Enter a number, 0 to stop: "))

    if number == 0:
        break

    print("You entered:", number)

print("while True loop ended")

print()


# --------------------------------
# 12. Menu-Based Example
# --------------------------------

choice = 0

while choice != 3:

    print("1. Say Hello")
    print("2. Say Bye")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Hello")

    elif choice == 2:
        print("Bye")

    elif choice == 3:
        print("Program Ended")

    else:
        print("Invalid Choice")

    print()


# --------------------------------
# 13. Count Even and Odd Numbers
# --------------------------------

i = 1
even_count = 0
odd_count = 0

while i <= 10:

    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    i += 1

print("Even Count:", even_count)
print("Odd Count:", odd_count)