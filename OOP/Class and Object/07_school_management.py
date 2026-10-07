# ==========================================
# OOP - MULTIPLE CLASSES SCHOOL MANAGEMENT
# ==========================================


# 1. Student Class

class Student:

    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def show_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Department:", self.department)


# 2. Teacher Class

class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def show_info(self):
        print("Name:", self.name)
        print("Subject:", self.subject)


# 3. School Class

class School:

    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_school_info(self):
        print("School Name:", self.school_name)
        print("Total Students:", len(self.students))
        print("Total Teachers:", len(self.teachers))

    def show_students(self):
        print("Student List")

        for student in self.students:
            student.show_info()
            print("--------------------")

    def show_teachers(self):
        print("Teacher List")

        for teacher in self.teachers:
            teacher.show_info()
            print("--------------------")


# 4. Creating Student Objects

student1 = Student("Junayed", 101, "CSE")
student2 = Student("Jayon", 102, "BBA")
student3 = Student("Sadman", 103, "EEE")


# 5. Creating Teacher Objects

teacher1 = Teacher("Mr. Ahmed", "Python")
teacher2 = Teacher("Ms. Sara", "Mathematics")


# 6. Creating School Object

school = School("ABC School")


# 7. Adding Students to School

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)


# 8. Adding Teachers to School

school.add_teacher(teacher1)
school.add_teacher(teacher2)


# 9. Showing School Information

school.show_school_info()

print("====================")


# 10. Showing All Students

school.show_students()


# 11. Showing All Teachers

school.show_teachers()