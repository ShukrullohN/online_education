from db_connect import Database
def create_table():
    student_table = """
        CREATE TABLE student(
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(50),
            password VARCHAR(20),
            contact_url VARCHAR(50),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())
    """

    mentor_table = """
        CREATE TABLE mentor(
            mentor_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(50),
            password VARCHAR(20),
            contact_url VARCHAR(50),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())
    """

    lenguage_table = """
        CREATE TABLE language(
            language_id SERIAL PRIMARY KEY,
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())
    """
    course_status_table = """
        CREATE TABLE course_status(
            course_status_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now())
    """

    speciality_table = """
        CREATE TABLE speciality(
            speciality_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now())
    """

    course_table = """
        CREATE TABLE course(
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description TEXT,
            rating FLOAT,
            active_students INT,
            mentor_id INT REFERENCES student(student_id),
            lenguage_id INT REFERENCES language(language_id),
            price NUMERIC,
            course_status_id INT REFERENCES course_status(course_status_id),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())
    """

    comment_table = """
        CREATE TABLE comment(
            comment_id SERIAL PRIMARY KEY,
            text TEXT,
            student_id INT REFERENCES student(student_id),
            course_id INT REFERENCES course(course_id))
    """

    payment_table = """
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            course_id INT REFERENCES course(course_id),
            student_id INT REFERENCES student(student_id),
            amound NUMERIC,
            card_number INT,
            create_date TIMESTAMP DEFAULT now())
    """

    data = {
        "student":  student_table,
        "mentor_table":  mentor_table,
        "lenguage_table":  lenguage_table,
        "course_status_table":  course_status_table,
        "speciality_table":  speciality_table,
        "course_table":  course_table,
        "comment_table":  comment_table,
        "payment_table":  payment_table
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")

if __name__ == "__main__":
    create_table()