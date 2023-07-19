from django.db import models
from .detailed_data import DELIVERY_DURATION
from authentication.models import MyUser
# Create your models here.


class Gig(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, default="I will")
    description = models.TextField(max_length=2999)
    images = models.ImageField(upload_to="gig images")
    video = models.FileField(upload_to="gig videos", null=True, blank=True)
    document = models.FileField(upload_to="gig documents", null=True, blank=True)
    category = models.CharField(max_length=45)
    sub_category = models.CharField(max_length=45)
    service_type = models.CharField(max_length=45, null=True, blank=True)
    search_tags = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class BasicPackage(models.Model):
    gig = models.OneToOneField(Gig, on_delete=models.CASCADE, related_name="basic_package")
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=125)
    delivery = models.CharField(choices=DELIVERY_DURATION, max_length=3)
    pages = models.IntegerField()
    revisions = models.IntegerField()
    content_upload = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class StandardPackage(models.Model):
    gig = models.OneToOneField(Gig, on_delete=models.CASCADE, related_name="standard_package")
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=125)
    delivery = models.CharField(choices=DELIVERY_DURATION, max_length=3)
    pages = models.IntegerField()
    revisions = models.IntegerField()
    content_upload = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class PremiumPackage(models.Model):
    gig = models.OneToOneField(Gig, on_delete=models.CASCADE, related_name="premium_package")
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=125)
    delivery = models.CharField(choices=DELIVERY_DURATION, max_length=3)
    pages = models.IntegerField()
    revisions = models.IntegerField()
    content_upload = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
