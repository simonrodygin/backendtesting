import random
import pdb

def test_grades_list(uni_service, clean_uni):
    grades = []
    student_ids = []
    teacher_ids = []
    for _ in range(3):
        student = uni_service.make_random_student()
        teacher = uni_service.make_random_teacher()
        grade = random.randint(0, 5)
        uni_service.make_grade(student_id=student.id, teacher_id=teacher.id, grade=grade)
        grades.append(grade)
        student_ids.append(student.id)
        teacher_ids.append(teacher.id)

    
    grades_data = uni_service.get_grades_list()
    assert len(grades_data) == 3
    for i in range(3):
        assert grades_data[i]['student_id'] == student_ids[i], f"Expected {student_ids[i]}, got {grades_data[i]['student_id']}"
        assert grades_data[i]['teacher_id'] == teacher_ids[i], f"Expected {teacher_ids[i]}, got {grades_data[i]['teacher_id']}"
        assert grades_data[i]['grade'] == grades[i], f"Expected {grades[i]}, got {grades_data[i]['grade']}"