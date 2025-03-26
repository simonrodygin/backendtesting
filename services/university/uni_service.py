from utils.session_utils import SessionUtils
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.helpers.grade_helper import GradeHelper
from services.university.models import PostStudentRequest
from services.university.models import PostGroupRequest
from services.university.models import PostTeacherRequest
from services.university.models import PostGradeRequest
from faker import Faker
import random
from services.university.models.degree import Degree
from typing import get_args

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
        group_data = PostGroupRequest(name=faker.word())
        response = self.group_helper.post_group(data=group_data.model_dump())
        return response

    def make_random_teacher(self):
        teacher_data = PostTeacherRequest(first_name=faker.name(), last_name=faker.name(), subject=faker.word())
        response = self.teacher_helper.post_teacher(data=teacher_data.model_dump())
        return response
    
    def make_random_student(self):
        groups_amount = len(self.group_helper.get_groups_list())
        if groups_amount == 0:
            self.make_random_group()
        
        student_data = PostStudentRequest(
            first_name=faker.name(),
            last_name=faker.name(),
            group_id=random.randint(1, groups_amount),
            email=faker.email(),
            phone=faker.phone_number(),
            degree=Degree(degree=random.choice(get_args(Degree.degree)))
        )

        response = self.student_helper.post_student(data=student_data.model_dump())
        return response
    
    def make_grade(self, student_id: int, teacher_id: int, grade: int):
        grade_data = PostGradeRequest(
            student_id=student_id,
            teacher_id=teacher_id,
            grade=grade
        )
        response = self.grade_helper.post_grade(data=grade_data.model_dump())
        return response
    
    def clean(self):
        for i in range(len(self.group_helper.get_groups_list())):
            self.group_helper.delete_group(i + 1)
        for i in range(len(self.teacher_helper.get_teachers_list())):
            self.teacher_helper.delete_teacher(i + 1)
        for i in range(len(self.student_helper.get_students_list())):
            self.student_helper.delete_student(i + 1)
        for i in range(len(self.grade_helper.get_grades_list())):
            self.grade_helper.delete_grade(i + 1)