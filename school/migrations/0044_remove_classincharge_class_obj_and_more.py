# Generated by Django 5.0.2 on 2024-03-06 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0043_rename_period_eight_from_timing_period_from_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classincharge',
            name='class_obj',
        ),
        migrations.RemoveField(
            model_name='classincharge',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='ClassAndTiming',
        ),
        migrations.DeleteModel(
            name='ClassIncharge',
        ),
    ]
