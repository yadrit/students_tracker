# Generated by Django 2.2.9 on 2020-01-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='num_of_students',
            field=models.CharField(max_length=3),
        ),
    ]
