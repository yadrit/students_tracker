from django.core.management.base import BaseCommand
from students.models import Student
from faker import Faker
import random

# In order to see the results run in console 'python manage.py gen_hundred' command w/o parameters
# it will create additional 100 students in DB

class Command(BaseCommand):
    help = 'Creates 100 students when performing command from console'

    def handle(self, *args, **options):
        for i in range(100):
            fake = Faker()
            student = Student(first_name=fake.name(), last_name=fake.name(), birth_date=fake.date(), email=fake.email(),
                              telephone=random.randint(1111111, 9999999))
            student.save()

