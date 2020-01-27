from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from students.models import Student, Group
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class StudentAdminForm(ModelForm):
    class Meta():
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone', 'grade')

    # Make email to be unique
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Student.objects.filter(email__iexact=email).exclude(email__iexact=self.instance.email).exists()

        if email_exists:
            raise ValidationError(f'{email} is already used')
        return email

    # Make telephone to be unique
    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        telephone_exists = Student.objects.filter(telephone__iexact=telephone)\
            .exclude(telephone__iexact=self.instance.telephone).exists()

        if telephone_exists:
            raise ValidationError(f'{telephone} is already in use')
        return telephone

class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data

        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)

        # Logging into txt file (works but slow)

        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")

        with open("logfile.txt", "a") as f:
            f.write("Current Timestamp : " + timestampStr + "\n")
            f.write("Subject: " + subject + "\n")
            f.write("Message: " + message + "\n")
            f.write("From: " + email_from + "\n")
            f.write("Recipients: " + ', '.join(recipient_list) + "\nEnd\n\n")
            f.close()
