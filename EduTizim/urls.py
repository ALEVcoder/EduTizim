from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("lesson/", include("schedule.urls")),
    path("payment/", include("payment.urls")),
]

admin.site.site_header = 'EduTizim my project in DRF'
admin.site.site_title = 'EduTizim'