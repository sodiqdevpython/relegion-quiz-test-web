# Generated by Django 5.0 on 2023-12-19 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_theme'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'Mavzu', 'verbose_name_plural': 'Mavzular'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='average_test_solve_time',
        ),
    ]
