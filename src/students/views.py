from django.http import HttpResponse

from students.models import Student


def gen_student(request):
    student = Student.gen_fake()
    data = f'{student.first_name} {student.last_name}'
    return HttpResponse(data)
