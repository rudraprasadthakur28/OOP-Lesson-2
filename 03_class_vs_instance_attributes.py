class Student:
    college = "Techno India"      # Class Attribute

    def __init__(self, name, age):
        self.name = name          # Instance Attribute
        self.age = age            # Instance Attribute

# student1.name → Rudra
# student2.name → Rahul

# student1.college → Techno India
# student2.college → Techno India

# Class Attribute = Common/shared data

# Instance Attribute = Object-specific data

student1 = Student("Rudra", 27)
student2 = Student("Rahul", 22)

print(student1.name)
print(student2.name)
print(student1.college)
print(student2.college)

class Employee:
    company = "ABC Ltd"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"{self.name} works at {self.company} and earns {self.salary}")

employee1 = Employee("Rudra", 30000)
employee1.show_details()