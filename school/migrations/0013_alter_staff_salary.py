# Generated by Django 5.0.2 on 2024-02-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_alter_staff_contract_details_alter_staff_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='salary',
            field=models.CharField(max_length=20),
        ),
    ]
