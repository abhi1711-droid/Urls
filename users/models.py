import random
import string

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserModel(AbstractUser):
    phone = models.CharField(null=True, unique=True, max_length=10)
    REQUIRED_FIELDS = ["phone"]

    def __str__(self):
        return self.phone


Get_User = get_user_model()


def generate_link():
    new_link = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return new_link


class Url(models.Model):
    original_link = models.URLField(max_length=500)
    short_link = models.CharField(max_length=50, default=generate_link, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    created_by = models.ForeignKey(Get_User, on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return self.original_link

    def clicked(self):
        self.clicks += 1
        self.save()
