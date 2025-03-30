import random
from logger.logger import Logger

def test_grades_list(uni_service, clean_uni):
    grades = []
    student_ids = []
    teacher_ids = []
    for i in range(3):
        Logger.info(f"### Step 1.{i + 1}.1 Creating student {i}")
        student = uni_service.make_random_student()
        Logger.info(f"### Step 1.{i + 1}.2 Creating teacher {i}")
        teacher = uni_service.make_random_teacher()
        Logger.info(f"### Step 1.{i + 1}.3 Creating grade {i}")
        grade = random.randint(0, 5)
        uni_service.make_grade(student_id=student.id, teacher_id=teacher.id, grade=grade)
        grades.append(grade)
        student_ids.append(student.id)
        teacher_ids.append(teacher.id)

    
    Logger.info("### Step 2 Get all grades")
    grades_data = uni_service.get_grades_list()
    assert len(grades_data) == 3
    for i in range(3):
        assert grades_data[i]['student_id'] == student_ids[i], f"Expected {student_ids[i]}, got {grades_data[i]['student_id']}"
        assert grades_data[i]['teacher_id'] == teacher_ids[i], f"Expected {teacher_ids[i]}, got {grades_data[i]['teacher_id']}"
        assert grades_data[i]['grade'] == grades[i], f"Expected {grades[i]}, got {grades_data[i]['grade']}"