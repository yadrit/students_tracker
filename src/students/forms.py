from django.forms import forms, ModelForm
from students.models import Student, Group


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'