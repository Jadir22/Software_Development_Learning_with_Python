# ==========================================
# STRING IMMUTABILITY AND STRING METHODS
# ==========================================


# 1. String and Index

name = "Rahim"

print("Name:", name)
print("First Character:", name[0])
print("Last Character:", name[-1])

print("--------------------")


# 2. String is Immutable

name = "Rahim"

# name[0] = "K"   # This would cause an error

name = "K" + name[1:]

print("New Name:", name)

print("--------------------")


# 3. upper() and lower()

text = "Hello Python"

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

print("--------------------")


# 4. capitalize() and title()

text = "hello PYTHON programming"

print("Capitalized:", text.capitalize())
print("Title:", text.title())

print("--------------------")


# 5. strip()

student_name = "   Rahim Islam   "

clean_name = student_name.strip()

print("Original:", student_name)
print("Clean Name:", clean_name)

print("--------------------")


# 6. replace()

sentence = "I like Java"

new_sentence = sentence.replace("Java", "Python")

print("Original:", sentence)
print("After Replace:", new_sentence)

print("--------------------")


# 7. find() and index()

message = "I love Python programming"

print("Python Position using find():", message.find("Python"))
print("Python Position using index():", message.index("Python"))

print("--------------------")


# 8. count()

word = "banana"

print("Number of a:", word.count("a"))

print("--------------------")


# 9. startswith() and endswith()

email = "student@gmail.com"

print("Starts with student:", email.startswith("student"))
print("Ends with .com:", email.endswith(".com"))

print("--------------------")


# 10. split()

student_data = "Rahim,22,CSE,3.75"

student_list = student_data.split(",")

print("Student Data List:", student_list)

print("--------------------")


# 11. join()

subjects = ["Python", "Java", "C++"]

subject_text = ", ".join(subjects)

print("Subjects:", subject_text)

print("--------------------")


# 12. isalpha(), isdigit(), isalnum()

name = "Rahim"
age = "22"
username = "Rahim123"

print("Name contains only letters:", name.isalpha())
print("Age contains only digits:", age.isdigit())
print("Username is letters/numbers:", username.isalnum())

print("--------------------")


# 13. Practical User Input Example

username = input("Enter username: ")

username = username.strip().lower()

print("Clean Username:", username)

print("--------------------")


# 14. Practical Validation Example

age = input("Enter your age: ")

if age.isdigit():
    print("Valid Age:", age)
else:
    print("Invalid age. Please enter numbers only.")