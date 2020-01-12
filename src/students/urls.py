from django.urls import path

from students.views import (gen_student, students,
                            gen_group, groups, students_add,
                            groups_add, students_edit, contact)


urlpatterns = [
    path('gen_fake/', gen_student),
    path('list/', students, name='students'),
    path('gen_group/', gen_group),
    path('groups/', groups),
    path('add/', students_add, name='students-add'),
    path('groups/add/', groups_add),
    path('edit/<int:pk>/', students_edit, name='students-edit'),
    path('contact/', contact, name='contact')
]