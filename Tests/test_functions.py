import functions


def setup_function():
    functions.students = []


def teardown_function():
    functions.delete_file()


def test_add_student_should_add_a_single_student_given_a_single_id_and_name():
    # arrange
    student_id = 123
    student_name = "Kevin"

    # act
    assert len(functions.students) == 0

    functions.add_student(student_id, student_name)

    # assert
    assert len(functions.students) == 1


def test_add_student_should_add_three_students_given_three_ids_and_names():
    # arrange
    student_id_1 = 123
    student_name_1 = "Kevin"
    student_id_2 = 456
    student_name_2 = "Kim"
    student_id_3 = 789
    student_name_3 = "Attie"

    # act
    assert len(functions.students) == 0

    functions.add_student(student_id_1, student_name_1)
    functions.add_student(student_id_2, student_name_2)
    functions.add_student(student_id_3, student_name_3)

    # assert
    assert len(functions.students) == 3


def test_get_students_titlecase_should_return_one_titlecased_name_given_one_lowercase_name():
    # arrange
    functions.students.append({"student_id": 123, "student_name": "kevin"})

    # act
    titlecase_students = functions.get_students_titlecase()

    # assert
    assert len(titlecase_students) == 1
    assert titlecase_students == ["Kevin"]


def test_save_file_should_create_a_students_file_with_one_name_given_a_single_student_name():
    # arrange

    # act
    functions.save_file("Kevin")
    functions.read_file()

    # assert
    assert len(functions.students) == 1
    assert functions.students[0]["student_name"] == "Kevin\n"
