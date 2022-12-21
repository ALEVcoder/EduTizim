from django.urls import path

from .views import LessonTableApiView

urlpatterns = [
    path("data/", LessonTableApiView.as_view(), name='lesson_data'),
]