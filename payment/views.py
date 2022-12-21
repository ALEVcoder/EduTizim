from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from users.models import Student
from payment.serializers import PaymentSerializer
from payment.models import Payment


class AdminCheckApiView(CreateAPIView):
    queryset = Payment.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = Student.objects.filter(user_id=int(serializer.data.get('student'))).first()
            user.user_payment = serializer.data.get('amount')
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)