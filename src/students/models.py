from django.db import models
from datetime import datetime
from faker import Faker
import random
from random import randint

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
        student = cls(first_name='D', last_name='K', birth_date=datetime.now().date(), email='asdas@gmail.com', telephone='+41x21oas4212')
        student.save()

# 6.1 Add Faker module, return fake students in console

    @classmethod
    def gen_fake(cls):
        fake = Faker()
        student = cls(first_name=fake.first_name(), last_name=fake.last_name(), birth_date=fake.date(), email=fake.email(),
                      telephone=random.randint(1111111, 9999999))
        student.save()
        return student

# 6.2 Create command which will generate 100 of students - it should run as custom django-admin command
# and add students to DB
# ---Check gen_hundred.py class---

# 6.3 Create class Group and fields in it

class Group(models.Model):
    group_code = models.CharField(max_length=20)
    num_of_students = models.CharField(max_length=3)
    faculty = models.CharField(max_length=50)
    start_year = models.CharField(max_length=4)
    senior_last_name = models.CharField(max_length=20)
    senior_phone = models.CharField(max_length=16)

    def get_group_info(self):
        return f'{self.group_code} | {self.faculty} | {self.start_year} | {self.num_of_students}'

    @classmethod
    def generate_group(cls):
        fake = Faker()
        group = cls(group_code=fake.license_plate(), faculty=fake.bs(), start_year=fake.year(), num_of_students=randint(0, 50) )
        group.save()
        return group