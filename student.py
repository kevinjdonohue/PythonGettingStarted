students = []


class Student:
    # class attribute -- e.g. static - not instance based
    school_name = "Springfield Elementary"

    # constructor
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        students.append(self)

    # string representation of the object
    # what about __repr__?
    def __str__(self):
        return "Student: " + self.student_name

    def get_name_capitalize(self):
        return self.student_name.capitalize()

    def get_school_name(self):
        return self.school_name
