# Generated by Django 2.2.9 on 2020-01-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_code', models.CharField(max_length=20)),
                ('num_of_students', models.IntegerField(max_length=3)),
                ('faculty', models.CharField(max_length=50)),
                ('start_year', models.DateField()),
                ('senior_last_name', models.CharField(max_length=20)),
                ('senior_phone', models.CharField(max_length=16)),
            ],
        ),
    ]
