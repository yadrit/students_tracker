from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from teachers.models import Teacher


class BaseTeacherForm(ModelForm):
    # Make email to be unique
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Teacher.objects.filter(email__iexact=email).exclude(email__iexact=self.instance.email).exists()

        if email_exists:
            raise ValidationError(f'{email} is already used')
        return email

    # Make telephone to be unique and contain only digits
    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        telephone_exists = Teacher.objects.filter(telephone__iexact=telephone)\
            .exclude(telephone__iexact=self.instance.telephone).exists()

        if telephone.isdigit():
            if telephone_exists:
                raise ValidationError(f'{telephone} is already in use')
            return telephone
        else:
            raise ValidationError('Telephone number should contain only digits')


    # Make first name start from capital letter
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].capitalize()
        return first_name


    # Make last name start from capital letter
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].capitalize()
        return last_name


class TeachersAddForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdminForm(BaseTeacherForm):
    class Meta():
        model = Teacher
        fields = ('id', 'email', 'degree', 'first_name', 'last_name', 'telephone')


class TeachersAddForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
