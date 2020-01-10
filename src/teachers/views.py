from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from teachers.forms import TeachersAddForm
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
        queryset = queryset.filter(Q(first_name__icontains=fn) |
                                   Q(last_name__icontains=fn) |
                                   Q(email__icontains=fn))

    for teacher in queryset:
        response += teacher.get_teacher_info() + '<br>'

    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})


# Logic for Teachers webform


def teachers_add(request):
    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    else:
        form = TeachersAddForm()

    return render(request,
                  'teachers_add.html',
                  context={'form': form})
