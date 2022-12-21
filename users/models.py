from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=14, unique=True)

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["first_name","last_name"]

    def __str__(self):
        return self.phone + ' | ' + str(self.first_name) + ' | ' + str(self.last_name)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' | ' + str(self.user.last_name)

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user_payment = models.FloatField(default=0)

    def __str__(self):
        return self.user.first_name + ' | ' + str(self.user_payment)

