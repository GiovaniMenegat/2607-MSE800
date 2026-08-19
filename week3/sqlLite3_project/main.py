from database import create_table
from student_manager import populate_students, populate_courses, populate_lectures, populate_enrollment, enroll_students, count_students, students_more_than_one_course


def main():
    create_table()
    populate_students()
    populate_courses()
    populate_lectures()
    populate_enrollment()
    enroll_students()
    count_students()
    students_more_than_one_course()

if __name__ == "__main__":
    main()
