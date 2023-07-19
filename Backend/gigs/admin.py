from django.contrib import admin
from .models import Gig, BasicPackage, StandardPackage, PremiumPackage
# Register your models here.


@admin.register(Gig)
class GigAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'category', 'sub_category']


@admin.register(BasicPackage)
class BasicPackageAdmin(admin.ModelAdmin):
    list_display = ['id', "gig", "name"]


@admin.register(StandardPackage)
class StandardPackageAdmin(admin.ModelAdmin):
    list_display = ['id', "gig", "name"]


@admin.register(PremiumPackage)
class PremiumPackageAdmin(admin.ModelAdmin):
    list_display = ['id', "gig", "name"]
