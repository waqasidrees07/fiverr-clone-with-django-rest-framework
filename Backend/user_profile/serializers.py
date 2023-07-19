from rest_framework import serializers
from .models import MyUserProfile, Education, Skills, Certification, Language
from authentication.serializers import MyUserSerializer


class MyUserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUserProfile
        fields = ("full_name", 'profile_picture', 'description', 'country')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["language_name", "language_level"]


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ["certificate", "certified_from", "year"]


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ["skill_name", "experience_level"]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ["title", "major_subject", "country_name", "institute_name", "year_of_graduation"]


class MyUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUserProfile
        fields = '__all__'
