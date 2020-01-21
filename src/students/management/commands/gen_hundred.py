from django.core.management.base import BaseCommand
from students.models import Student, Group
import random
# In order to see the results run in console
# 'python manage.py gen_hundred' command w/o parameters
# it will create additional 100 students in DB


class Command(BaseCommand):
    help = 'Creates 100 students ' \
           'when performing command from console'

    def handle(self, *args, **options):
        Group.objects.all().delete()
        Student.objects.all().delete()

        groups = [Group.objects.create(group_code=f'name_{i}')
                  for i in range(10)]

        # for student in Student.objects.all()
        for j in range(100):
            student = Student.gen_fake()
            student.group = random.choice(groups)
            student.save()