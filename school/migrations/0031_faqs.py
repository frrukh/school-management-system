# Generated by Django 5.0.2 on 2024-03-01 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0030_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
