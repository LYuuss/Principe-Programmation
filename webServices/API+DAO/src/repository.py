from db import get_connection

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

r = get_all_students()

print(r)

def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = f"SELECT * FROM students WHERE id = {student_id}"
    cursor.execute(query, (student_id,))

    stud = cursor.fetchone()

    cursor.close()
    conn.close()

    return stud

def add_student(table, prenom, age):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = f"INSERT INTO {table} (prenom, age) VALUES \n('{prenom}', '{age}')"
    cursor.execute(query, (prenom, age,))

    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return student


"""
sur l'api Flask :
from flask import Flask, jsonify, request 
import repository
def get_students():
    students = repository.get_all_students()
    return jsonify(students), 200

def get_student_by_id():
    student = repository.get_student_by_id()
    return jsonify(students), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port =5001, debug=true)
"""