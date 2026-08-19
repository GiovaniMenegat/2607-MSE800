import sqlite3

def create_connection():
    conn = sqlite3.connect("yoobee.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            birth_date TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS enrollment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_code TEXT NOT NULL,
            date_of_enrollment TEXT NOT NULL,
            course_name TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS lecture (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            time TEXT NOT NULL,
            date TEXT NOT NULL,
            lecture_name TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS enrolls (
            student_id INT,
            enrollment_id INT,
            lecture_id INT,
            FOREIGN KEY (student_id) REFERENCES student(id) ON DELETE CASCADE,
            FOREIGN KEY (enrollment_id) REFERENCES enrollment(id) ON DELETE CASCADE,
            FOREIGN KEY (lecture_id) REFERENCES lecture(id) ON DELETE CASCADE,
            PRIMARY KEY (student_id, enrollment_id, lecture_id)
        );

        CREATE TABLE IF NOT EXISTS lecturer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lecture_id TEXT NOT NULL,
            lecturer_lastname TEXT NOT NULL,
            lecturer_firstname TEXT NOT NULL,
            lecturer_email TEXT NOT NULL,
            lecturer_address TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_code TEXT NOT NULL,
            subject_unit TEXT NOT NULL,
            subject_udsc TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS lectures (
            lecturer_id INT,
            subjects_id INT,
            lecture_id INT,
            FOREIGN KEY (lecturer_id) REFERENCES lecturer(id) ON DELETE CASCADE,
            FOREIGN KEY (subjects_id) REFERENCES subjects(id) ON DELETE CASCADE,
            FOREIGN KEY (lecture_id) REFERENCES lecture(id) ON DELETE CASCADE,
            PRIMARY KEY (lecturer_id, subjects_id, lecture_id)
        );
    ''')
    conn.commit()
    conn.close()
