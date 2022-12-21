from rest_framework import serializers

from users.models import CustomUser, Teacher


class SearchUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class SearchUserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id"]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["user"]