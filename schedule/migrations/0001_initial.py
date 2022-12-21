# Generated by Django 4.1.3 on 2022-12-20 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('finish_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Yoqlama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('lessontable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessontable', to='schedule.lessontable')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yoqlama_student', to='users.student')),
            ],
        ),
        migrations.AddField(
            model_name='lessontable',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_room', to='schedule.room'),
        ),
        migrations.AddField(
            model_name='lessontable',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_student', to='users.student'),
        ),
        migrations.AddField(
            model_name='lessontable',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_subject', to='schedule.subject'),
        ),
        migrations.AddField(
            model_name='lessontable',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_teacher', to='users.teacher'),
        ),
        migrations.AddField(
            model_name='lessontable',
            name='weekday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_day', to='schedule.weekday'),
        ),
    ]
