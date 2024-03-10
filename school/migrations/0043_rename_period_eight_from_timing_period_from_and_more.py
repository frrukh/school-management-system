# Generated by Django 5.0.2 on 2024-03-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0042_timing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timing',
            old_name='period_eight_from',
            new_name='period_from',
        ),
        migrations.RenameField(
            model_name='timing',
            old_name='period_eight_to',
            new_name='period_to',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_five_from',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_five_to',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_four_from',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_four_to',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_one_from',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_one_to',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_seven_from',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_seven_to',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_six_from',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_six_to',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_three_from',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_three_to',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_two_from',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='period_two_to',
        ),
        migrations.AddField(
            model_name='timing',
            name='period_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]