from utils.session_utils import SessionUtils
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.helpers.grade_helper import GradeHelper
from university.models import PostStudentRequest
from university.models import PostGroupRequest
from university.models import PostTeacherRequest
from university.models import PostGradeRequest
from faker import Faker
from utils.json_utils import JsonUtils

faker = Faker()

class UniService():
    SERVICE_URL = 'http://127.0.0.1:8001/'
    
    def __init__(self, session_utils: SessionUtils):
        self.session_utils = session_utils
        
        self.student_helper = StudentHelper(self.session_utils)
        self.group_helper = GroupHelper(self.session_utils)
        self.teacher_helper = TeacherHelper(self.session_utils)
        self.grade_helper = GradeHelper(self.session_utils)


    def make_every_entity_random_data(self, number_of_entities: int):
        for i in range(number_of_entities):
            group_data = PostGroupRequest(name=faker.word())
            teacher_data = PostTeacherRequest(first_name=faker.name(), last_name=faker.name(), subject=faker.word())
            student_data = PostStudentRequest(
                first_name=faker.name(),
                last_name=faker.name(),
                group_id=i + 1,
                email=faker.email(),
                phone=faker.phone_number(),
                degree='Bachelor'
            )
            grade_data = PostGradeRequest(
                student_id=i + 1,
                grade=faker.random_int(min=0, max=5),
                teacher_id=i + 1
            )
            
            self.student_helper.post_student(data=student_data.model_dump())
            self.group_helper.post_group(data=group_data.model_dump())
            self.teacher_helper.post_teacher(data=teacher_data.model_dump())
            self.grade_helper.post_grade(data=grade_data.model_dump())

    def delete_every_entity(self, number_of_entities: int):
        for i in range(number_of_entities):
            self.student_helper.delete_student(student_id=i + 1)
            self.group_helper.delete_group(group_id=i + 1)
            self.teacher_helper.delete_teacher(teacher_id=i + 1)
            self.grade_helper.delete_grade(grade_id=i + 1)