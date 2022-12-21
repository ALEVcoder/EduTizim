from django.urls import path

from users.views import SearchUserInfoApiView

urlpatterns = [
    path("", SearchUserInfoApiView.as_view(), name='user_search'),
]