import json
import os


def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    with open(input_json_path) as f:
        students = json.load(f)
    student_in_course = []
    for _, student_values in students.items():
        if course_name in student_values["registered_courses"]:
            student_in_course.append(student_values["student_name"])
    return student_in_course


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    with open(input_json_path) as f:
        students = json.load(f)
    output_courses = {}
    for _, student_value in students.items():
        for course in student_value["registered_courses"]:
            if course in output_courses:
                output_courses[course] = output_courses[course] + 1
            else:
                output_courses[course] = 1
    output_courses = dict(sorted(output_courses.items()))
    with open(output_file_path, 'w') as f_out:
        for course_name, student_amount in output_courses.items():
            line_in_file = '"%s" %s\n' % (course_name, student_amount)
            f_out.write(line_in_file)



def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    json_files = [file for file in os.listdir(json_directory_path) if file.endswith('.json')]
    lecturers_courses = {}
    for current_file in json_files:
        with open(os.path.join(json_directory_path, current_file)) as f:
            course_by_semester = json.load(f)
        for _, course_value in course_by_semester.items():
            for lecturer in course_value["lecturers"]:
                if lecturer in lecturers_courses:
                    lecturers_courses[lecturer].add(course_value["course_name"])
                else:
                    lecturers_courses[lecturer] = {course_value["course_name"]}
    lecturers_courses = {lecturer: list(course) for (lecturer, course) in lecturers_courses.items()}

    with open(output_json_path, 'w') as f_out:
        f_out.write(json.dumps(lecturers_courses))



