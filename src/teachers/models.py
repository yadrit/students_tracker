from django.db import models
from faker import Faker
import random


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    telephone = models.CharField(max_length=16)
    degree = models.CharField(max_length=20)

    def get_teacher_info(self):
        return f'{self.first_name} | {self.last_name} | {self.degree} | {self.email} | {self.telephone}'

    @classmethod
    def generate_teacher(cls):
        fake = Faker()
        teacher = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      degree=random.choice(['A.S.', 'M.S.', 'Ph.D.', 'J.D.', 'M.D.']),
                      email=fake.email(),
                      telephone=random.randint(1111111, 9999999))
        teacher.save()
        return teacher

    # Overriding in order to see group_code instead of 'Group object' in admin
    def __str__(self):
        return f'{self.degree} {self.first_name} {self.last_name}'
