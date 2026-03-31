from db import get_connection

# ---------- AUTH ----------

def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )
    conn.commit()

    cursor.close()
    conn.close()


def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


# ---------- STUDENT CRUD ----------

def add_student(name, age, course, marks):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, course, marks) VALUES (%s,%s,%s,%s)",
        (name, age, course, marks)
    )
    conn.commit()

    cursor.close()
    conn.close()


def get_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def search_students(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE %s",
        ('%' + name + '%',)
    )
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def update_student(student_id, name, age, course, marks):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=%s, age=%s, course=%s, marks=%s WHERE id=%s",
        (name, age, course, marks, student_id)
    )
    conn.commit()

    cursor.close()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (student_id,)
    )
    conn.commit()

    cursor.close()
    conn.close()