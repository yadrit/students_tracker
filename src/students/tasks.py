from celery import shared_task, task
from django.core.mail import send_mail
from time import sleep
import datetime

from students.models import Student, Logger


@shared_task
def add(a, b):
    print('ADD WORKS!')
    sleep(10)
    print(a + b)
    return a + b


@shared_task
def send_email_async(subject, message, email_from, recipient_list, student):
    student_obj = Student.objects.get(id=student)
    send_mail(subject, message, student_obj.email,
              email_from, recipient_list,
              fail_silently=False)


@task
def flush_logger():
    Logger.objects.all().filter(created__gte=datetime.datetime.now()-datetime.timedelta(days=7)).delete()

