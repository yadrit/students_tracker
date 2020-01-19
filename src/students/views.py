from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from students.forms import StudentsAddForm, GroupsAddForm, ContactForm
from students.models import Student, Group
from django.urls import reverse

# Filter by first_name


def gen_student(request):
    student = Student.gen_fake()
    data = f'{student.first_name} {student.last_name}'
    return HttpResponse(data)


def students(request):
    queryset = Student.objects.all()

    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__istartswith=fn)

    return render(request,
                  'students_list.html',
                  context={'students': queryset})

# Filter by first_name, last_name and email


def gen_group(request):
    group = Group.generate_group()
    data = f'{group.group_code} | {group.faculty} | {group.start_year} | {group.num_of_students}'
    return HttpResponse(data)


def groups(request):
    queryset = Group.objects.all()

    gc = request.GET.get('group_code')
    if gc:
        queryset = queryset.filter(group_code__contains=gc)

    return render(request,
                  'groups_list.html',
                  context={'groups': queryset})

# Logic for Students webform


def students_add(request):
    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm()

    return render(request,
                  'students_add.html',
                  context={'form': form})

# Logic for Groups webform


def groups_add(request):
    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm()

    return render(request,
                  'groups_add.html',
                  context={'form': form})

# Logic for Students edit webform


def students_edit(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student with id {pk} not found')

    if request.method == 'POST':
        form = StudentsAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm(instance=student)

    return render(request,
                  'students_edit.html',
                  context={'form': form, 'pk': pk})


# Logic for contact form


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = ContactForm()

    return render(request,
                  'contact.html',
                  context={'form': form})


# Logic for Groups edit webform


def groups_edit(request, pk):
    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f'Group with id {pk} not found')

    if request.method == 'POST':
        form = GroupsAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm(instance=group)

    return render(request,
                  'groups_edit.html',
                  context={'form': form, 'pk': pk})
