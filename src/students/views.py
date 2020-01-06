from django.http import HttpResponse
from django.shortcuts import render

from students.models import Student, Group


def gen_student(request):
    student = Student.gen_fake()
    data = f'{student.first_name} {student.last_name}'
    return HttpResponse(data)

def students(request):
    queryset = Student.objects.all()
    response = ''

    fn = request.GET.get('first_name')
    if fn:
        # __contains LIKE %{}%
        # queryset = queryset.filter(first_name__contains=fn)

        # __endswith LIKE %{}
        # queryset = queryset.filter(first_name__endswith=fn)

        # __startswith LIKE {}%
        # queryset = queryset.filter(first_name__startswith=fn)

        # __istartswith LIKE {}%
        queryset = queryset.filter(first_name__istartswith=fn)

    for student in queryset:
        response += student.get_info() + '<br>'

    return render(request,
                  'students_list.html',
                  context={'students_list': response})

def gen_group(request):
    group = Group.generate_group()
    data = f'{group.group_code} | {group.faculty} | {group.start_year} | {group.num_of_students}'
    return HttpResponse(data)

def groups(request):
    queryset = Group.objects.all()
    response = ''

    gc = request.GET.get('group_code')
    if gc:
        queryset = queryset.filter(group_code__contains=gc)

    for group in queryset:
        response += group.get_group_info() + '<br>'

    return render(request,
                  'groups_list.html',
                  context={'groups_list': response})