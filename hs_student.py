from student import Student


class HighSchoolStudent(Student):
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a high school student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()

        return original_value + "-HS"
