students = []

def read_file():
    try:
        file_to_open = open("students.txt", "r")
        for student in read_students(file_to_open):
            students.append(student)
        file_to_open.close()
    except Exception:
        print("Could not read file")


def read_students(file_to_open):
    for line in file_to_open:
        yield line


read_file()
print(students)