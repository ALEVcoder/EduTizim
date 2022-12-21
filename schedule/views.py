from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from .models import LessonTable, Yoqlama

from .serializers import LessonTableSerializer

User = get_user_model()

class LessonTableApiView(ListAPIView):
    queryset = LessonTable.objects.all()

    def get(self, request, *args, **kwargs):
        phone = request.query_params.get('phone')
        date = request.query_params.get('date')
        week = request.query_params.get('week').title()
        part_obj = Yoqlama.objects.filter(student__user__phone=phone, date=date).first()
        print(part_obj)
        if part_obj:
            lesson = self.get_queryset().filter(weekday__name=week).first()
            serializer = LessonTableSerializer(lesson, many=False)
            result = serializer.data
            result.update({'is_part': part_obj.is_part})
            print(result)
            return Response(result, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


