# ==========================================
# PYTHON OOP - STATIC ATTRIBUTE,
# STATIC METHOD AND CLASS METHOD
# ==========================================


class Student:

    # 1. Class / Static Attributes
    university = "AIUB"
    student_count = 0

    # 2. Constructor
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

        Student.student_count += 1

    # 3. Instance Method
    def show_info(self):
        print("Name:", self.name)
        print("Mark:", self.mark)
        print("University:", Student.university)

    # 4. Class Method
    @classmethod
    def show_university(cls):
        print("University:", cls.university)

    # 5. Class Method to Change Class Attribute
    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

    # 6. Class Method to Show Student Count
    @classmethod
    def show_student_count(cls):
        print("Total Students:", cls.student_count)

    # 7. Static Method
    @staticmethod
    def is_valid_mark(mark):
        if mark >= 0 and mark <= 100:
            return True
        else:
            return False

    # 8. Alternative Constructor
    @classmethod
    def from_string(cls, data):
        name, mark = data.split("-")
        return cls(name, int(mark))


# 9. Creating Objects

student1 = Student("Rahim", 80)
student2 = Student("Karim", 75)


# 10. Using Instance Method

student1.show_info()

print("--------------------")

student2.show_info()

print("--------------------")


# 11. Using Class Method

Student.show_university()

Student.show_student_count()

print("--------------------")


# 12. Changing Class Attribute

Student.change_university("NSU")

Student.show_university()

print("--------------------")


# 13. Using Static Method

print("Is 90 a valid mark?", Student.is_valid_mark(90))
print("Is 150 a valid mark?", Student.is_valid_mark(150))

print("--------------------")


# 14. Creating Object with Class Method

student3 = Student.from_string("Jadir-95")

student3.show_info()

print("--------------------")

Student.show_student_count()