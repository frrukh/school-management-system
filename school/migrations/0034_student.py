# Generated by Django 5.0.2 on 2024-03-04 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0033_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Name', max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('guardian_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=500)),
                ('date_of_enrollment', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('emergency_phone', models.CharField(max_length=100)),
                ('previous_school', models.CharField(blank=True, max_length=200, null=True)),
                ('password1', models.CharField(default='passwords', max_length=100)),
                ('password2', models.CharField(default='passwords', max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.gender')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.grade')),
                ('guardian_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.guardianrelation')),
            ],
        ),
    ]
