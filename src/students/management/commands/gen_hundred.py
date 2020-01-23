from django.core.management.base import BaseCommand
from students.models import Student, Group
from teachers.models import Teacher
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
        Teacher.objects.all().delete()

        # Create 100 students
        students = [Student.gen_fake() for i in range(100)]
        print(len(students))

        # Create 10 groups
        # groups = [Group.objects.create(group_code=f'name_{i}')
        #           for i in range(10)]
        groups = [Group.generate_group() for i in range(10)]

        # Create 10 teachers
        teachers = [Teacher.generate_teacher() for i in range(10)]

        # Update students - Add to random Groups
        for student in students:
            student.group = random.choice(groups)
            student.save()

        # Updated groups - Added curator and senior
        for group in groups:
            group.curator = random.choice(teachers)
            group.senior = random.choice(students)
            group.save()


