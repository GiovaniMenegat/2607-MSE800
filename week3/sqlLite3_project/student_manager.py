from database import create_connection
import sqlite3

def populate_students():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO student (first_name, last_name, birth_date) VALUES ('Lucas', 'Silva', '2005-04-12'), ('Beatriz', 'Santos', '2006-09-23'), ('Gabriel', 'Oliveira', '2005-11-02'), ('Mariana', 'Souza', '2007-01-15'), ('Rodrigo', 'Lima', '2006-07-30');")
        conn.commit()
        print("Students added successfully.")
    except sqlite3.IntegrityError:
        print("Student already added.")
    conn.close()

def populate_courses():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lecture (subject, time, date, lecture_name) VALUES ('MSE800', '09:00', '2026-08-20', 'Software Development Lifecycle Models'), ('MSE801', '13:00', '2026-08-21', 'Quantitative vs Qualitative Research Methods'), ('MSE802', '10:30', '2026-08-24', 'Introduction to Quantum Gates and Circuits');")
        conn.commit()
        print("Courses added successfully.")
    except sqlite3.IntegrityError:
        print("Course already added.")
    conn.close()

def populate_lectures():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lectures (lecturer_id, subjects_id, lecture_id) VALUES (1, 1, 1), (2, 2, 2);")
        conn.commit()
        print("Lectures added successfully.")
    except sqlite3.IntegrityError:
        print("Lecture already added.")
    conn.close()

def populate_enrollment():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO enrollment (student_code, date_of_enrollment, course_name) VALUES ('1', '2026-02-10', 'MSE800'), ('2', '2026-02-10', 'MSE801'), ('3', '2026-02-11', 'MSE800'), ('4', '2026-02-11', 'MSE802'), ('5', '2026-02-12', 'MSE801');")
        conn.commit()
        print("Enrollments populated successfully.")
    except sqlite3.IntegrityError:
        print("Something went wrong.")
    conn.close()

def enroll_students():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO enrolls (student_id, enrollment_id, lecture_id) VALUES (1, 1, 1), (2, 2, 2), (3, 3, 1), (4, 4, 3), (5, 5, 2);")
        conn.commit()
        print("Students enrolled successfully.")
    except sqlite3.IntegrityError:
        print("Something went wrong.")
    conn.close()

def count_students():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT l.subject AS course, COUNT(DISTINCT en.student_id) AS num_students FROM enrolls en JOIN lecture l ON en.lecture_id = l.id GROUP BY l.subject;")
        results = cursor.fetchall()
        print("How many students are registered in each course: ")
        for course, num_students in results:
            print(f"{course}: {num_students} student(s)")
    except sqlite3.IntegrityError:
        print("Something went wrong.")
    conn.close()

def students_more_than_one_course():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT s.id, s.first_name, s.last_name, COUNT(DISTINCT en.lecture_id) AS num_courses FROM student s JOIN enrolls en ON s.id = en.student_id GROUP BY s.id, s.first_name, s.last_name HAVING COUNT(DISTINCT en.lecture_id) > 1;")
        results = cursor.fetchall()
        print("List the names and student IDs of students who have enrolled in more than one course: ")
        for student_id, first_name, last_name, num_courses in results:
            print(f"{first_name} {last_name} (ID: {student_id}) - {num_courses} courses")
    except sqlite3.IntegrityError:
        print("Something went wrong.")
    conn.close()