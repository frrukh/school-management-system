# Generated by Django 5.0.2 on 2024-02-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_rename_subject_staff_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='contract_details',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='experience',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
