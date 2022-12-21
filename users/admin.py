from django.contrib import admin

from users.models import CustomUser, Teacher, Student

admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Student)
