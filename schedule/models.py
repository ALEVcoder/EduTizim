from django.db import models

from users.models import Student, Teacher


class WeekDay(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class LessonTable(models.Model):
    student = models.ForeignKey(Student, related_name='lesson_student', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='lesson_teacher', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="lesson_room", on_delete=models.CASCADE)
    weekday = models.ForeignKey(WeekDay, related_name="lesson_day",on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="lesson_subject", on_delete=models.CASCADE)
    start_time = models.TimeField(null=True, blank=True)
    finish_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.student.user.first_name + ' | ' + str(self.student.user.phone)  + ' | ' + str(self.teacher.user.first_name)
        

class Yoqlama(models.Model):
    lessontable = models.ForeignKey(LessonTable, related_name='lessontable', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='yoqlama_student', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_part = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Yoqlama'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student.user.first_name + ' | ' + str(self.lessontable.subject)

    
