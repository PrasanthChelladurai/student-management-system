from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host="localhost", user="root", password="", database="student_db")
cursor = conn.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    age = request.form["age"]
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
