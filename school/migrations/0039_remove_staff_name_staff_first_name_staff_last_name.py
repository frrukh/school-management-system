# Generated by Django 5.0.2 on 2024-03-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0038_studentapplication_is_registered_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='name',
        ),
        migrations.AddField(
            model_name='staff',
            name='first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='staff',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
