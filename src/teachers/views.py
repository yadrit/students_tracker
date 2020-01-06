from django.http import HttpResponse
from django.shortcuts import render
from teachers.models import Teacher

def gen_teacher(request):
    teacher = Teacher.generate_teacher()
    data = f'{teacher.first_name} {teacher.last_name} {teacher.degree} {teacher.email} {teacher.telephone}'
    return HttpResponse(data)

def teachers(request):
    queryset = Teacher.objects.all()
    response = ''
    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__contains=fn)

    for teacher in queryset:
        response += teacher.get_teacher_info() + '<br>'

    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})
