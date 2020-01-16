from django.urls import path


from teachers.views import gen_teacher, teachers, teachers_add, teachers_edit

urlpatterns = [
    path('gen/', gen_teacher),
    path('list/', teachers, name='teachers'),
    path('add/', teachers_add, name='teachers-add'),
    path('edit/<int:pk>/', teachers_edit, name='teachers-edit'),
]
