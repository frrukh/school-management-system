# Generated by Django 5.0.2 on 2024-02-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='previous_school',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
