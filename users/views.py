from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from users.serializers import SearchUserInfoSerializer, SearchUserPaymentSerializer

User = get_user_model()

class SearchUserInfoApiView(ListAPIView):
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        number = request.query_params.get('q')
        is_payment = request.query_params.get('is_payment')
        if is_payment and number:
            users = self.get_queryset().filter(phone__icontains=number)
            serializer = SearchUserPaymentSerializer(users, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

        if number:
            users = self.get_queryset().filter(phone__icontains=number)
            serializer = SearchUserInfoSerializer(users, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)