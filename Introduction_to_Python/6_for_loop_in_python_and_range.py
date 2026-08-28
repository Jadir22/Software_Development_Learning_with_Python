# For Loop and range() in Python


# 1. Basic range(stop)

for i in range(5):
    print(i)

print()


# 2. range(start, stop)

for i in range(1, 6):
    print(i)

print()


# 3. range(start, stop, step)

for i in range(2, 11, 2):
    print(i)

print()


# 4. Reverse Counting

for i in range(5, 0, -1):
    print(i)

print()


# 5. Even and Odd Check

for i in range(1, 6):

    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

print()


# 6. Sum Using For Loop

total = 0

for i in range(1, 6):
    total += i

print("Total:", total)

print()


# 7. Multiplication Table

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# For Loop with List in Python


# 1. Print all items from a list

names = ["Rahim", "Karim", "Sakib", "Nayeem"]

for name in names:
    print(name)

print()


# 2. Print numbers from a list

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)

print()


# 3. Find sum of list items

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print("Total:", total)

print()


# 4. Check even and odd numbers from a list

numbers = [3, 8, 11, 14, 20]

for number in numbers:

    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

print()


# 5. Print list items using range()

fruits = ["Apple", "Mango", "Banana", "Orange"]

for i in range(len(fruits)):
    print(i, fruits[i])