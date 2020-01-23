from django.core.management.base import BaseCommand
from students.models import Student, Group
from teachers.models import Teacher
import random

class Command(BaseCommand):
    help = 'Creates 100 students ' \
           'when performing command from console'

    def handle(self, *args, **options):
        Student.objects.all().delete()


        groups = list(Group.group_code)

        for j in range(100):
             student = Student.gen_fake()
             student.group = random.choice(groups)
             student.save()

        # for t in range(groups):
        #     t.curator = random.choice(curators)
        #     t.save()