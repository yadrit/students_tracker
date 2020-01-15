from django.forms import ModelForm, Form, EmailField, CharField
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

        f = open("logfile.txt", "a")
        f.write("Current Timestamp : " + timestampStr + "\n")
        f.write("Subject: " + subject + "\n")
        f.write("Message: " + message + "\n")
        f.write("From: " + email_from + "\n")
        f.write("Recipients: " + ', '.join(recipient_list) + "\nEnd\n\n")
        f.close()