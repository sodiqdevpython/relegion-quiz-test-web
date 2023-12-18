# Generated by Django 5.0 on 2023-12-17 14:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text="Agar savolingizni klaviaturada yozib bo'lmasa rasmini kiriting !", verbose_name='Savolni kiriting')),
                ('image_question', models.ImageField(blank=True, help_text="Agar klaviaturada yoza olmasangiz savolni rasmga olib faqat rasmini qo'ying", null=True, upload_to='images/', verbose_name="Agar savolingizni yozib bo'lmasa rasmini kiriting")),
            ],
            options={
                'verbose_name': "Yangi savol qo'shish",
                'verbose_name_plural': "Savol qo'shish",
            },
        ),
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Mavzu nomi')),
                ('tugatish', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': "Yangi test qo'shish",
                'verbose_name_plural': 'Yangi test tuzish',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='GroupUNI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('overall_ball', models.PositiveIntegerField(default=0)),
                ('group_students', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_score', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('average_test_solve_time', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('which_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.groupuni')),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profillar',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_right', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question')),
            ],
            options={
                'verbose_name': 'Test javoblari',
                'verbose_name_plural': 'Testlar javoblari',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.quizmodel'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_question', models.IntegerField()),
                ('corrent_question', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('spend_time', models.PositiveIntegerField(blank=True, null=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.quizmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Test natijalari',
                'verbose_name_plural': 'Test natijalari',
                'ordering': ['-corrent_question'],
                'unique_together': {('user', 'quiz')},
            },
        ),
    ]
