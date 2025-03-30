import statistics
from logger.logger import Logger
from services.university.models.grade.get_grades_response_success import GetGradesResponseSuccess
from services.university.models.grade.get_grades_stats_response_success import GetGradesStatsResponseSuccess
from faker import Faker
import pytest

faker = Faker()

class TestGrades():
    @pytest.mark.skip
    def test_grades_list(uni_readiness_check, uni_service, clean_uni):
        grades = []
        student_ids = []
        teacher_ids = []
        test_entities = 3
        Logger.info("### Step 1 make entitites")
        for i in range(test_entities):
            grades_model_object = uni_service.make_random_grade()
            
            grades.append(grades_model_object.grade)
            student_ids.append(grades_model_object.student_id)
            teacher_ids.append(grades_model_object.teacher_id)

        
        Logger.info("### Step 2 Get all grades")
        grades_data = uni_service.get_grades_list()
        GetGradesResponseSuccess.model_validate(grades_data)
        assert len(grades_data) == test_entities
        for i in range(test_entities):
            assert grades_data[i]['student_id'] == student_ids[i], f"Expected {student_ids[i]}, got {grades_data[i]['student_id']}"
            assert grades_data[i]['teacher_id'] == teacher_ids[i], f"Expected {teacher_ids[i]}, got {grades_data[i]['teacher_id']}"
            assert grades_data[i]['grade'] == grades[i], f"Expected {grades[i]}, got {grades_data[i]['grade']}"

    @pytest.mark.skip
    def test_grades_stats_general(uni_readiness_check, uni_service, clean_uni):
        Logger.info("### Step 1 make entitites")
        grades_list = []
        test_entities = 10
        for i in range(test_entities):
            grades_model_object = uni_service.make_random_grade()
            grades_list.append(grades_model_object.grade)

        Logger.info('### Step 2 Get statistics')
        stats = GetGradesStatsResponseSuccess.model_validate(uni_service.grade_helper.get_stats().json())
        assert stats.count == test_entities, f"Count in stats is {stats.count} expected to be {test_entities}"
        assert stats.min == min(grades_list), f"Min grade in stats is {stats.min} expected to be {min(grades_list)}"
        assert stats.max == max(grades_list), f"Max grade in stats is {stats.max} expected to be {max(grades_list)}"
        assert stats.avg == statistics.mean(grades_list), f"Avg grade in stats is {stats.avg} expected to be {statistics.mean(grades_list)}"


    def test_grades_stats_by_teacher(uni_readiness_check, uni_service, clean_uni):
        Logger.info("### Step 1 make entitites")
        grades_list = []
        test_entities = 3
        teacher = uni_service.make_random_teacher()
        for i in range(test_entities):    
            grades_model_object = uni_service.make_random_grade(teacher_id = teacher.id)
            grades_list.append(grades_model_object.grade)
   
        Logger.info('### Step 2 Vary data')
        grades_model_object = uni_service.make_random_grade()

        Logger.info('### Step 3 Get statistics')
        stats = GetGradesStatsResponseSuccess.model_validate(uni_service.grade_helper.get_stats('teacher_id', teacher.id).json())
        assert stats.count == test_entities, f"Count in stats is {stats.count} expected to be {test_entities}"
        assert stats.min == min(grades_list), f"Min grade in stats is {stats.min} expected to be {min(grades_list)}"
        assert stats.max == max(grades_list), f"Max grade in stats is {stats.max} expected to be {max(grades_list)}"
        assert stats.avg == statistics.mean(grades_list), f"Avg grade in stats is {stats.avg} expected to be {statistics.mean(grades_list)}"
    