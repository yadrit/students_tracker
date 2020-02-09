from django.urls import path
from django.contrib.auth import views as auth_views

from students.views import (gen_student, students,
                            gen_group, groups, students_add,
                            groups_add, students_edit, groups_edit, contact, register,
                            custom_login)


urlpatterns = [
    path('gen_fake/', gen_student),
    path('list/', students, name='students'),
    path('add/', students_add, name='students-add'),
    path('edit/<int:pk>/', students_edit, name='students-edit'),
    path('gen_group/', gen_group),
    path('groups/', groups, name='groups'),
    path('groups/add/', groups_add, name='groups-add'),
    path('groups/edit/<int:pk>', groups_edit, name='groups-edit'),
    path('contact/', contact, name='contact'),
    path('login/', custom_login, name='login'),
    path('register/', register, name='register'),
]
