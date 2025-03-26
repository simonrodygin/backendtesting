import random

def test_grades_list(uni_service):
    grades = []
    for _ in range(3):
        student = uni_service.make_random_student()
        teacher = uni_service.make_random_teacher()
        grade = random.randint(1, 10)
        grades.append(grade)
        uni_service.make_grade(student_id=student['id'], teacher_id=teacher['id'], grade=grade)
    
    grades = uni_service.grade_helper.get_grades_list()
    assert len(grades) == 3
    for i in range(3):
        assert grades[i]['student_id'] == i + 1
        assert grades[i]['teacher_id'] == i + 1
        assert grades[i]['grade'] == grades[i]
        assert grades[i]['id'] == i + 1

    uni_service.clean()