class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"{self.name} ({self.roll_number}): {self.cgpa}"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
student1 = Student("Alice", "001", 3.8)
student2 = Student("Bob", "002", 3.5)
student3 = Student("Charlie", "003", 3.9)
student4 = Student("David", "004", 3.7)

students = [student1, student2, student3, student4]

sorted_students = sort_students(students)

for student in sorted_students:
    print(student)