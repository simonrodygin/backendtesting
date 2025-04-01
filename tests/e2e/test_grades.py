import statistics
from logger.logger import Logger
from services.university.models.grade.get_grades_response_success import GetGradesResponseSuccess
from services.university.models.grade.get_grades_stats_response_success import GetGradesStatsResponseSuccess
from faker import Faker
import pytest
import pdb

faker = Faker()

class TestGrades():
    test_entities = 3
    
    @pytest.mark.skip
    def test_grades_list(self, uni_readiness_check, uni_service):
        grades = []
        student_ids = []
        teacher_ids = []
        Logger.info("### Step 1 make entitites")
        for _ in range(self.test_entities):
            grades_model_object = uni_service.make_random_grade()
            
            grades.append(grades_model_object.grade)
            student_ids.append(grades_model_object.student_id)
            teacher_ids.append(grades_model_object.teacher_id)
    
        Logger.info("### Step 2 Get all grades")
        grades_data = uni_service.get_grades_list()
        GetGradesResponseSuccess.model_validate(grades_data)
        return grades_data, grades, student_ids, teacher_ids    
    
    @pytest.mark.grades_list
    def test_grades_list_len(self, uni_readiness_check, uni_service, clean_uni):
        grades_data, _, _, _ = self.test_grades_list(uni_readiness_check, uni_service)
        assert len(grades_data) == self.test_entities
    
    @pytest.mark.grades_list
    def test_grades_list_student_id(self, uni_readiness_check, uni_service, clean_uni):
        grades_data, _, student_ids, _ = self.test_grades_list(uni_readiness_check, uni_service)    
        for i in range(self.test_entities):
            assert grades_data[i]['student_id'] == student_ids[i], f"Expected {student_ids[i]}, got {grades_data[i]['student_id']}"
    
    @pytest.mark.grades_list
    def test_grades_list_teacher_id(self, uni_readiness_check, uni_service, clean_uni):
        grades_data, _, _, teacher_ids = self.test_grades_list(uni_readiness_check, uni_service)    
        for i in range(self.test_entities):
            assert grades_data[i]['teacher_id'] == teacher_ids[i], f"Expected {teacher_ids[i]}, got {grades_data[i]['teacher_id']}"
    
    @pytest.mark.grades_list
    def test_grades_list_grade(self, uni_readiness_check, uni_service, clean_uni):
        grades_data, grades, _, _ = self.test_grades_list(uni_readiness_check, uni_service)    
        for i in range(self.test_entities):
            assert grades_data[i]['grade'] == grades[i], f"Expected {grades[i]}, got {grades_data[i]['grade']}"
    
    @pytest.mark.skip
    def test_grades_stats_general(self, uni_readiness_check, uni_service):
        Logger.info("### Step 1 make entitites")
        grades_list = []
        for i in range(self.test_entities):
            grades_model_object = uni_service.make_random_grade()
            grades_list.append(grades_model_object.grade)

        Logger.info('### Step 2 Get statistics')
        stats = GetGradesStatsResponseSuccess.model_validate(uni_service.grade_helper.get_stats().json())
        return stats, grades_list
    
    @pytest.mark.grades_stats_general
    def test_grades_stats_general_count(self, uni_readiness_check, uni_service, clean_uni):   
        stats, _ = self.test_grades_stats_general(uni_readiness_check, uni_service)
        assert stats.count == self.test_entities, f"Count in stats is {stats.count} expected to be {self.test_entities}"
    
    @pytest.mark.grades_stats_general
    def test_grades_stats_general_min(self, uni_readiness_check, uni_service, clean_uni):   
        stats, grades_list = self.test_grades_stats_general(uni_readiness_check, uni_service)
        assert stats.min == min(grades_list), f"Min grade in stats is {stats.min} expected to be {min(grades_list)}"
    
    @pytest.mark.grades_stats_general
    def test_grades_stats_general_max(self, uni_readiness_check, uni_service, clean_uni):   
        stats, grades_list = self.test_grades_stats_general(uni_readiness_check, uni_service)
        assert stats.max == max(grades_list), f"Max grade in stats is {stats.max} expected to be {max(grades_list)}"
    
    @pytest.mark.grades_stats_general
    def test_grades_stats_general_max(self, uni_readiness_check, uni_service, clean_uni):   
        stats, grades_list = self.test_grades_stats_general(uni_readiness_check, uni_service)
        assert stats.avg == statistics.mean(grades_list), f"Avg grade in stats is {stats.avg} expected to be {statistics.mean(grades_list)}"
    
    @pytest.mark.skip
    def test_grades_stats_by_teacher(self, uni_readiness_check, uni_service):
        Logger.info("### Step 1 make entitites")
        grades_list = []
        teacher = uni_service.make_random_teacher()
        for i in range(self.test_entities):    
            grades_model_object = uni_service.make_random_grade(teacher_id = teacher.id)
            grades_list.append(grades_model_object.grade)
   
        Logger.info('### Step 2 Vary data')
        grades_model_object = uni_service.make_random_grade()

        Logger.info('### Step 3 Get statistics')
        stats = GetGradesStatsResponseSuccess.model_validate(uni_service.grade_helper.get_stats({'teacher_id': teacher.id}).json())
        return stats, grades_list

    @pytest.mark.grades_stats_by_teacher
    def test_grades_stats_by_teacher_count(self, uni_readiness_check, uni_service, clean_uni):   
        stats, _ = self.test_grades_stats_by_teacher(uni_readiness_check, uni_service)
        assert stats.count == self.test_entities, f"Count in stats is {stats.count} expected to be {self.test_entities}"

    @pytest.mark.grades_stats_by_teacher
    def test_grades_stats_by_teacher_min(self, uni_readiness_check, uni_service, clean_uni):   
        stats, grades_list = self.test_grades_stats_by_teacher(uni_readiness_check, uni_service)
        assert stats.min == min(grades_list), f"Min grade in stats is {stats.min} expected to be {min(grades_list)}"

    @pytest.mark.grades_stats_by_teacher
    def test_grades_stats_by_teacher_max(self, uni_readiness_check, uni_service, clean_uni):   
        stats, grades_list = self.test_grades_stats_by_teacher(uni_readiness_check, uni_service)
        assert stats.max == max(grades_list), f"Max grade in stats is {stats.max} expected to be {max(grades_list)}"
    
    @pytest.mark.grades_stats_by_teacher
    def test_grades_stats_by_teacher_avg(self, uni_readiness_check, uni_service, clean_uni):   
        stats, grades_list = self.test_grades_stats_by_teacher(uni_readiness_check, uni_service)
        assert stats.avg == statistics.mean(grades_list), f"Avg grade in stats is {stats.avg} expected to be {statistics.mean(grades_list)}"         