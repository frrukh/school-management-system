# Generated by Django 5.0.2 on 2024-02-16 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_student_previous_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='emergency_phone',
        ),
    ]
