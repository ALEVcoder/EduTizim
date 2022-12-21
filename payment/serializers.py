from rest_framework import serializers
from users.serializers import TeacherSerializer

from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["student", "subject", "type", "amount"]
    
