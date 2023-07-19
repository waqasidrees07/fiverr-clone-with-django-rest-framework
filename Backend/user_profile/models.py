from django.db import models
from .detailed_data import (
    LANGUAGE_LEVELS,
    EXPERIENCE_LEVELS,
    user_join_date,
    EDUCATION_TITLE,
)
from authentication.models import MyUser


# Create your models here.
class Language(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    language_name = models.CharField(max_length=255)
    language_level = models.CharField(choices=LANGUAGE_LEVELS, max_length=100)

    def __str__(self):
        return str(self.language_name)


class Skills(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    skill_name = models.CharField(max_length=255)
    experience_level = models.CharField(choices=EXPERIENCE_LEVELS, max_length=100)

    def __str__(self):
        return str(self.skill_name)


class Education(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(choices=EDUCATION_TITLE, max_length=100)
    major_subject = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    institute_name = models.CharField(max_length=255)
    year_of_graduation = models.IntegerField(null=True, blank=True)


class Certification(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    certificate = models.CharField(max_length=255)
    certified_from = models.CharField(max_length=255)
    year = models.IntegerField()


class MyUserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(
        default="default.png", upload_to="Profile Pictures"
    )
    description = models.TextField(null=True, blank=True)
    country = models.CharField(null=True, blank=True, max_length=255)
    member_since = models.CharField(default=user_join_date, max_length=255)
