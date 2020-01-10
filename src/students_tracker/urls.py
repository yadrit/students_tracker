"""students_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from students.views import gen_student, students, gen_group, groups, students_add, groups_add
from teachers.views import gen_teacher, teachers, teachers_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gen_fake/', gen_student),
    path('students/', students),
    path('gen_group/', gen_group),
    path('groups/', groups),
    path('gen_teacher/', gen_teacher),
    path('teachers/', teachers),
    path('students/add/', students_add),
    path('groups/add/', groups_add),
    path('teachers/add/', teachers_add)
]
