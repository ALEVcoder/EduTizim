from django.urls import path

from .views import AdminCheckApiView

urlpatterns = [
    path("", AdminCheckApiView.as_view(), name='user_payment'),
]