from django.db import models
from datetime import datetime
from faker import Faker
import random

"""
CREATE TABLE students_student (
    first_name varchar(20    
)
"""
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=16) # clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)

    def get_info(self):
        return f'{self.first_name} | {self.last_name} | {self.birth_date} | {self.email} | {self.telephone}'

    @classmethod
    def generate_student(cls):
        student = cls(first_name='D', last_name='K', birth_date=datetime.now().date(), email='asdas@gmail.com', telephone='12312312')
        student.save()

# 6.1 Add Faker module, return fake students in console

    @classmethod
    def gen_fake(cls):
        fake = Faker()
        student = cls(first_name=fake.name(), last_name=fake.name(), birth_date=fake.date(), email=fake.email(),
                      telephone=random.randint(1111111, 9999999))
        student.save()

# 6.2 Create command which will generate 100 of students - it should run as custom django-admin command
# and add students to DB
# ---Check gen_hundred.py class---

# 6.3 Create class Group and fields in it

class Group(models.Model):
    group_code = models.CharField(max_length=20)
    num_of_students = models.IntegerField(max_length=3)
    faculty = models.CharField(max_length=50)
    start_year = models.DateField()
    senior_last_name = models.CharField(max_length=20)
    senior_phone = models.CharField(max_length=16)