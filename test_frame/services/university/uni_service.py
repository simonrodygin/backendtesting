from test_frame.utils.session_utils import SessionUtils
from test_frame.services.university.helpers.student_helper import StudentHelper
from test_frame.services.university.helpers.group_helper import GroupHelper
from test_frame.services.university.helpers.teacher_helper import TeacherHelper
from test_frame.services.university.helpers.grade_helper import GradeHelper
from test_frame.services.university.models.student.post_student_request import PostStudentRequest
from test_frame.services.university.models.student.post_student_response_success import PostStudentResponseSuccess
from test_frame.services.university.models.group.post_group_request import PostGroupRequest
from test_frame.services.university.models.teacher.post_teacher_request import PostTeacherRequest
from test_frame.services.university.models.grade.post_grade_request import PostGradeRequest
from test_frame.services.university.models.grade.post_grade_response_success import PostGradeResponseSuccess
from test_frame.services.university.models.teacher.post_teacher_response_success import PostTeacherResponseSuccess
from faker import Faker
import random
from test_frame.services.university.models.degree_enum import DegreeEnum
from test_frame.services.university.models.subject_enum import SubjectEnum
from test_frame.services.university.models.group.post_group_response_success import PostGroupResponseSuccess
import string
from logger.logger import Logger
from test_frame.utils.confiig_reader import ConfigReader
from test_frame.test_frame.assets.constants import Constants

faker = Faker()
config_reader = ConfigReader()

class UniService:
    SERVICE_URL = 'http://127.0.0.1:8001/'
    
    def __init__(self, session_utils: SessionUtils):
        self.session_utils = session_utils
        
        self.student_helper = StudentHelper(self.session_utils)
        self.group_helper = GroupHelper(self.session_utils)
        self.teacher_helper = TeacherHelper(self.session_utils)
        self.grade_helper = GradeHelper(self.session_utils)

    def make_random_group(self) -> PostGroupResponseSuccess:
        group_data = PostGroupRequest(name=faker.word())
        response = self.group_helper.post_group(data=group_data.json())
        return PostGroupResponseSuccess(**response.json())

    def make_random_teacher(self) -> PostTeacherResponseSuccess:
        teacher_data = PostTeacherRequest(first_name=faker.name(), last_name=faker.name(), subject=random.choice(list(SubjectEnum)))
        response = self.teacher_helper.post_teacher(data=teacher_data.json())
        return PostTeacherResponseSuccess(**response.json())
    
    def make_random_student(self) -> PostStudentResponseSuccess:      
        group = self.make_random_group()
    
        student_data = PostStudentRequest(
            first_name=faker.name(),
            last_name=faker.name(),
            group_id=group.id,
            email=faker.email(),
            phone='+7' + ''.join(random.choices(string.digits, k=7)),
            degree=random.choice(list(DegreeEnum))
        )

        response = self.student_helper.post_student(data=student_data.json())
        return PostStudentResponseSuccess(**response.json())
    
    def make_grade(self, post_grade_request_data: PostGradeRequest) -> PostGradeResponseSuccess:
        response = self.grade_helper.post_grade(data=post_grade_request_data.dict())
        return PostGradeResponseSuccess(**response.json())
    
    def make_random_grade(self, teacher_id: int = None, student_id: int = None):
        if student_id is None:
            student = self.make_random_student()
            s_id = student.id
        else:
            s_id = student_id

        if teacher_id is None:
            teacher = self.make_random_teacher()
            t_id = teacher.id
        else:
            t_id = teacher_id
        grade = random.randint(Constants.MIN_GRADE, Constants.MAX_GRADE)  
        make_grade_req_data = PostGradeRequest(
            teacher_id = t_id,
            student_id = s_id,
            grade = grade
        )
        response = self.make_grade(make_grade_req_data)
        return response

    def clean_group(self):
        Logger.info('### Cleaning group university data')
        if len(self.get_groups_list()) != 0 and self.get_groups_list() is not None:
            for group in self.get_groups_list():
                self.group_helper.delete_group(group['id'])

    def clean_teacher(self):
        Logger.info('### Cleaning teacher university data')
        if len(self.get_teachers_list()) != 0 and self.get_teachers_list() is not None:
            for teacher in self.get_teachers_list():
                self.teacher_helper.delete_teacher(teacher['id'])

    def clean_student(self):
        Logger.info('### Cleaning student university data')
        if len(self.get_students_list()) != 0 and self.get_students_list() is not None:
            for student in self.get_students_list():
                self.student_helper.delete_student(student['id'])

    def clean_grades(self):
        Logger.info('### Cleaning grades university data')
        if len(self.get_grades_list()) != 0 and self.get_grades_list() is not None:
            for grade in self.get_grades_list():
                self.grade_helper.delete_grade(grade['id'])
    
    
    def clean(self):   
        self.clean_group()
        self.clean_teacher()  
        self.clean_student()
        self.clean_grades()

    def get_grades_list(self) -> list:
        try:
            return list(self.grade_helper.get_grades().json())
        except TypeError:
            return None
    
    def get_students_list(self) -> list:
        try:
            return list(self.student_helper.get_students().json())
        except TypeError:
            return None

    def get_teachers_list(self) -> list:
        try:
            return list(self.teacher_helper.get_teachers().json())
        except TypeError:
            return None
    
    def get_groups_list(self) -> list:
        try:
            return list(self.group_helper.get_groups().json())
        except TypeError:
            return None