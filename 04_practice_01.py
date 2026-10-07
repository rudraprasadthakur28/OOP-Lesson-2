class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

student1 = Student("Rudra")
student2 = Student("Rahul")

student1.college = "XYZ College"

print(student1.college)
print(student2.college)
print(Student.college)