import os

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


def save_file(student_name):
    try:
        file_to_save = open("students.txt", "a")
        file_to_save.write(student_name + "\n")
        file_to_save.close()
    except Exception:
        print("Could not save file!")


def read_file():
    try:
        file_to_read = open("students.txt", "r")
        student_id = 1
        for student_name in file_to_read.readlines():
            add_student(student_id, student_name)
            student_id += 1

        file_to_read.close()
    except Exception:
        print("Could not read file!")


def delete_file():
    try:
        if os.path.isfile("students.txt"):
            os.remove("students.txt")
            print("Removed students.txt")
    except Exception:
        print("Could not delete file!")


def student_prompt():
    return input("Do you want to add a student? (Yes|No) ").upper()


def handle_input():
    read_file()

    print_students_titlecase()

    enter_a_student = student_prompt()

    while enter_a_student == "YES":
        # student_id = input("Enter student ID: ")
        student_id = request_input_value("Enter student ID: ")
        # student_name = input("Enter student name: ")
        student_name = request_input_value("Enter student name: ")
        add_student(student_id, student_name)
        save_file(student_name)
        enter_a_student = student_prompt()

    if enter_a_student == "NO":
        print_students_titlecase()


def request_input_value(prompt):
    return input(prompt)


    # handle_input()

    # read_file()
    #
    # print_students_titlecase()
    #
    # student_id = input("Enter student ID: ")
    # student_name = input("Enter student name: ")
    #
    # add_student(student_id, student_name)
    #
    # save_file(student_name)
