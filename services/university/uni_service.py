from utils.session_utils import SessionUtils
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.helpers.grade_helper import GradeHelper
from services.university.models.student.post_student_request import PostStudentRequest
from services.university.models.student.post_student_response_success import PostStudentResponseSuccess
from services.university.models.group.group import Group
from services.university.models.teacher.post_teacher_request import PostTeacherRequest
from services.university.models.grade.post_grade_request import PostGradeRequest
from services.university.models.grade.post_grade_response_success import PostGradeResponseSuccess
from services.university.models.teacher.post_teacher_response_success import PostTeacherResponseSuccess
from faker import Faker
import random
from services.university.models.degree import Degree
from services.university.models.subject import Subject
from services.university.models.group.post_group_response_success import PostGroupResponseSuccess
import string
from logger.logger import Logger

faker = Faker()

class UniService():
    SERVICE_URL = 'http://127.0.0.1:8001/'
    
    def __init__(self, session_utils: SessionUtils):
        self.session_utils = session_utils
        
        self.student_helper = StudentHelper(self.session_utils)
        self.group_helper = GroupHelper(self.session_utils)
        self.teacher_helper = TeacherHelper(self.session_utils)
        self.grade_helper = GradeHelper(self.session_utils)

    def make_random_group(self):
        group_data = Group(name=faker.word())
        response = self.group_helper.post_group(data=group_data.json())
        return PostGroupResponseSuccess(**response.json())

    def make_random_teacher(self):
        teacher_data = PostTeacherRequest(first_name=faker.name(), last_name=faker.name(), subject=random.choice(list(Subject)))
        response = self.teacher_helper.post_teacher(data=teacher_data.json())
        return PostTeacherResponseSuccess(**response.json())
    
    def make_random_student(self):      
        group = self.make_random_group()
    
        student_data = PostStudentRequest(
            first_name=faker.name(),
            last_name=faker.name(),
            group_id=group.id,
            email=faker.email(),
            phone='+7' + ''.join(random.choices(string.digits, k=7)),
            degree=random.choice(list(Degree))
        )

        response = self.student_helper.post_student(data=student_data.json())
        return PostStudentResponseSuccess(**response.json())
    
    def make_grade(self, student_id: int, teacher_id: int, grade: int):
        grade_data = PostGradeRequest(
            student_id=student_id,
            teacher_id=teacher_id,
            grade=grade
        )
        response = self.grade_helper.post_grade(data=grade_data.dict())
        return PostGradeResponseSuccess(**response.json())
    
    def clean_group(self):
        Logger.info('### Cleaning group university data')
        if len(self.get_groups_list()) != 0:
            for group in self.get_groups_list():
                self.group_helper.delete_group(group['id'])   
    
    def clean(self):
        Logger.info('### Cleaning all university data')
        if len(self.get_groups_list()) != 0:
            for group in self.get_groups_list():
                self.group_helper.delete_group(group['id'])    
        
        if len(self.get_teachers_list()) != 0:
            for teacher in self.get_teachers_list():
                self.teacher_helper.delete_teacher(teacher['id'])

        if len(self.get_students_list()) != 0:
            for student in self.get_students_list():
                self.student_helper.delete_student(student['id'])
        
        if len(self.get_grades_list()) != 0:
            for grade in self.get_grades_list():
                self.grade_helper.delete_grade(grade['id'])
        Logger.info('### All university data clean')

    def get_grades_list(self) -> list:
        try:
            list(self.grade_helper.get_grades().json())
        except TypeError:
            return []

        return list(self.grade_helper.get_grades().json())
    
    def get_students_list(self) -> list:
        try:
            list(self.student_helper.get_students().json())
        except TypeError:
            return []
        
        return list(self.student_helper.get_students().json())
    
    def get_teachers_list(self) -> list:
        try:
            list(self.teacher_helper.get_teachers().json())
        except TypeError:
            return []
        
        return list(self.teacher_helper.get_teachers().json())
    
    def get_groups_list(self) -> list:
        try:
            list(self.group_helper.get_groups().json())
        except TypeError:
            return []
        
        return list(self.group_helper.get_groups().json())