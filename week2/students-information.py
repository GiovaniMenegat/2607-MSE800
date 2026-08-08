class Student:
    """Represents one student's personal information."""

    def __init__(self, full_name: str, age: int, address: str, student_id: str):
        self.full_name = full_name
        self.age = age
        self.address = address
        self.student_id = student_id

    def __str__(self):
        return (f"ID: {self.student_id} | Name: {self.full_name} | "
                f"Age: {self.age} | Address: {self.address}")

def collect_students(max_students=70):
    students = []
    print(f"Enter student details (up to {max_students}). Leave the name blank to stop.\n")

    while len(students) < max_students:
        full_name = input("Full name: ")
        if not full_name:
            break

        age = int(input("Age: "))
        address = input("Address: ")
        student_id = input("Student ID: ")

        students.append(Student(full_name, age, address, student_id))
        print(f"Added. ({len(students)} student(s) so far)\n")

    return students

if __name__ == "__main__":
    students = collect_students()

    students.sort(key=lambda student: student.age)

    print("\n--- All students, sorted by age ---")
    for student in students:
        print(student)
