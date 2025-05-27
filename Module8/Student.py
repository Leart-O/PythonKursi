class Student:
    school_name = "Digital School"
    # student_name = "Student"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student1 = Student("Alice", 15, "Python")
print(student1.course)

# student1 = Student()
# print(student1.school_name)
# print(student1.student_name)