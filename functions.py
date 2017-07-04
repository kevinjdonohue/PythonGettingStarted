students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["student_name"].title())

    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(student_id, student_name):
    student = {"student_id": student_id, "student_name": student_name}
    students.append(student)


def save_file(student):
    try:
        file_to_save = open("students.txt", "a")
        file_to_save.write(student + "\n")
        file_to_save.close()
    except Exception:
        print("Could not save file!")


def read_file():
    try:
        file_to_read = open("students.txt", "r")
        student_id = 1
        for student_name in file_to_read.readlines():
            add_student(student_id=student_id, student_name=student_name)
            student_id += 1

        file_to_read.close()
    except Exception:
        print("Could not read file!")


def student_prompt():
    return input("Do you want to add a student? (Yes|No) ").upper()


def handle_input():
    enter_a_student = student_prompt()

    while enter_a_student == "YES":
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        add_student(student_id, student_name)
        enter_a_student = student_prompt()

    if enter_a_student == "NO":
        print_students_titlecase()


handle_input()
