# ==========================================
# SET AND SET METHODS IN PYTHON
# ==========================================


# 1. Creating a Set

students = {"Rahim", "Karim", "Nadia"}

print("Students:", students)

print("--------------------")


# 2. Duplicate Values are Removed

numbers = {10, 20, 20, 30, 30, 30}

print("Unique Numbers:", numbers)

print("--------------------")


# 3. Empty Set

empty_set = set()

print("Empty Set:", empty_set)
print("Type:", type(empty_set))

print("--------------------")


# 4. add()

subjects = {"Python", "Java"}

subjects.add("C++")

print("After add:", subjects)

print("--------------------")


# 5. update()

subjects.update(["C#", "HTML", "CSS"])

print("After update:", subjects)

print("--------------------")


# 6. remove()

subjects.remove("Java")

print("After remove:", subjects)

print("--------------------")


# 7. discard()

subjects.discard("PHP")

print("After discard:", subjects)

print("--------------------")


# 8. pop()

numbers = {10, 20, 30, 40}

removed_number = numbers.pop()

print("Removed:", removed_number)
print("Remaining:", numbers)

print("--------------------")


# 9. copy()

original = {1, 2, 3}

copied = original.copy()

print("Original:", original)
print("Copied:", copied)

print("--------------------")


# 10. union()

class_a = {"Rahim", "Karim", "Nadia"}
class_b = {"Nadia", "Sakib", "Mim"}

all_students = class_a.union(class_b)

print("All Students:", all_students)

print("--------------------")


# 11. intersection()

common_students = class_a.intersection(class_b)

print("Common Students:", common_students)

print("--------------------")


# 12. difference()

only_class_a = class_a.difference(class_b)

print("Only in Class A:", only_class_a)

print("--------------------")


# 13. symmetric_difference()

different_students = class_a.symmetric_difference(class_b)

print("Not Common:", different_students)

print("--------------------")


# 14. Set Operators

a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

print("--------------------")


# 15. issubset() and issuperset()

small_set = {1, 2}
large_set = {1, 2, 3, 4}

print("Is Subset:", small_set.issubset(large_set))
print("Is Superset:", large_set.issuperset(small_set))

print("--------------------")


# 16. Looping Through a Set

languages = {"Python", "Java", "C++"}

for language in languages:
    print(language)

print("--------------------")


# 17. Checking Membership

if "Python" in languages:
    print("Python was found")

print("--------------------")


# 18. Removing Duplicate Values from a List

marks = [80, 70, 80, 90, 70, 85]

unique_marks = set(marks)

print("Original Marks:", marks)
print("Unique Marks:", unique_marks)

print("--------------------")


# 19. Practical Subject Example

rahim_subjects = {"Python", "Java", "C++"}
karim_subjects = {"Python", "Java", "C#"}

common_subjects = rahim_subjects & karim_subjects
all_subjects = rahim_subjects | karim_subjects
only_rahim = rahim_subjects - karim_subjects

print("Common Subjects:", common_subjects)
print("All Subjects:", all_subjects)
print("Only Rahim's Subjects:", only_rahim)

print("--------------------")


# 20. clear()

temporary_set = {1, 2, 3}

temporary_set.clear()

print("After clear:", temporary_set)