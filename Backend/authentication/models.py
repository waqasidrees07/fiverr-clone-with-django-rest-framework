from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    user_permissions = True
    groups = True

    def __str__(self):
        return self.username
