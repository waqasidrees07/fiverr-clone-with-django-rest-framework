from django.contrib import admin
from .models import Education, Skills, Language, Certification, MyUserProfile

# Register your models here.


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title", "major_subject", "year_of_graduation"]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "language_name", "language_level"]


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "skill_name", "experience_level"]


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "certificate", "certified_from", "year"]


@admin.register(MyUserProfile)
class MyUserProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "country", "member_since"]
