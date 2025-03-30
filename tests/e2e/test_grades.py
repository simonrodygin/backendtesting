import random
from logger.logger import Logger
from services.university.models.grade.get_grades_response_success import GetGradesResponseSuccess
from services.university.models.grade.post_grade_request import PostGradeRequest
from faker import Faker

faker = Faker()

class TestGrades():
    def test_grades_list(uni_readiness_check, uni_service, clean_uni):
        grades = []
        student_ids = []
        teacher_ids = []
        test_entities = 3
        Logger.info("### Step 1 make entitites")
        for i in range(test_entities):
            grades_object = uni_service.make_random_grade()
            
            grades.append(grades_object.grade)
            student_ids.append(grades_object.student_id)
            teacher_ids.append(grades_object.teacher_id)

        
        Logger.info("### Step 2 Get all grades")
        grades_data = uni_service.get_grades_list()
        GetGradesResponseSuccess.model_validate(grades_data)
        assert len(grades_data) == test_entities
        for i in range(test_entities):
            assert grades_data[i]['student_id'] == student_ids[i], f"Expected {student_ids[i]}, got {grades_data[i]['student_id']}"
            assert grades_data[i]['teacher_id'] == teacher_ids[i], f"Expected {teacher_ids[i]}, got {grades_data[i]['teacher_id']}"
            assert grades_data[i]['grade'] == grades[i], f"Expected {grades[i]}, got {grades_data[i]['grade']}"

    