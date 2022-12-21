from django.contrib import admin
from .models import WeekDay, Room, Subject, LessonTable, Yoqlama

admin.site.register(WeekDay)
admin.site.register(Room)
admin.site.register(Subject)
admin.site.register(LessonTable)
admin.site.register(Yoqlama)