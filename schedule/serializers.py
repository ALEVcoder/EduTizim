from rest_framework import serializers
from users.serializers import TeacherSerializer

from .models import LessonTable, Yoqlama, Room, WeekDay, Subject

class YoqlamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yoqlama
        fields = ["id", "lessontable", "date"]
    
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ["id"]

class WeekDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDay
        exclude = ["id"]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        exclude = ["id"]
    

class LessonTableSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True, many=False)
    subject = SubjectSerializer(read_only=True, many=False)
    weekday = WeekDaySerializer(read_only=True, many=False)
    class Meta:
        model = LessonTable
        fields = ["id", "weekday", "subject", "room", "start_time", "finish_time"]

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['teacher'] = f"{instance.teacher.user.first_name} {instance.teacher.user.last_name}"
        return res