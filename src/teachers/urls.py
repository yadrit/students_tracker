from django.contrib import admin
from django.urls import path, include


from teachers.views import gen_teacher, teachers, teachers_add

urlpatterns = [
    path('gen/', gen_teacher),
    path('list/', teachers),
    path('add/', teachers_add)
]