from flask import Flask, request, redirect, url_for, render_template

from student import Student

students = []

app = Flask(__name__)


# route decorator
@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        new_student_id = request.form.get("student_id", "")
        new_student_name = request.form.get("student_name", "")
        new_student_last_name = request.form.get("student_last_name", "")

        new_student = Student(student_id=new_student_id, student_name=new_student_name)
        students.append(new_student)

        return redirect(url_for("students_page"))

    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run()
