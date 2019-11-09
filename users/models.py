from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "OTHER"),
    )

    avatar = models.ImageField(null=True, blank=True)  # blank는 칸이 비워져도 save할 수 있도록.
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)  # default 또는 null값을 허용해 db가 알 수 있도록.
