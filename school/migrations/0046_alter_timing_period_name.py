# Generated by Django 5.0.2 on 2024-03-06 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0045_classandtiming_classincharge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing',
            name='period_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
