from django.shortcuts import redirect
from rest_framework.views import APIView
from .models import MyUserProfile, Language, Skills, Certification, Education
from rest_framework.permissions import IsAuthenticated
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from gigs.models import Gig
from gigs.serializers import GetGigSerializer


# Create your views here.


class UserProfileView(APIView):
    def get(self, request):
        user = self.request.user
        if user.email_verified == False:
            return redirect('email-verification')

        profile = MyUserProfile.objects.get(user=user)
        languages = Language.objects.filter(user=user)
        certificates = Certification.objects.filter(user=user)
        skills = Skills.objects.filter(user=user)
        education = Education.objects.filter(user=user)
        gigs = Gig.objects.filter(user=user)

        gigs_serializer = GetGigSerializer(gigs, many=True)
        profile_serializer = serializers.MyUserProfileSerializer(profile)
        languages_serializer = serializers.LanguageSerializer(languages, many=True)
        certificates_serializer = serializers.CertificationSerializer(certificates, many=True)
        skills_serializer = serializers.SkillsSerializer(skills, many=True)
        education_serializer = serializers.EducationSerializer(education, many=True)

        serialized_data = {
            "profile": profile_serializer.data,
            "user": user.username,
            "gigs": gigs_serializer.data,
            "languages": languages_serializer.data,
            "certificates": certificates_serializer.data,
            "skills": skills_serializer.data,
            "education": education_serializer.data
        }

        return Response({"user profile": serialized_data})


class MyUserProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MyUserProfile.objects.all()
    serializer_class = serializers.MyUserProfileUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user'

    def get_object(self):
        return self.queryset.get(user=self.request.user)


class LanguageCreateView(generics.CreateAPIView):
    queryset = Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LanguageUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        queryset = Language.objects.all()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('id'))

        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this object.")

        return obj


class LanguageDeleteView(generics.DestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        queryset = Language.objects.all()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('id'))

        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this object.")

        return obj


class SkillCreateView(generics.CreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = serializers.SkillsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SkillUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Skills.objects.all()
    serializer_class = serializers.SkillsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        queryset = Skills.objects.all()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('id'))

        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this object.")

        return obj


class SkillDeleteView(generics.DestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = serializers.SkillsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        queryset = Skills.objects.all()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('id'))

        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this object.")

        return obj


class EducationCreateView(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EducationUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        queryset = Education.objects.all()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('id'))

        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this object.")

        return obj


class EducationDeleteView(generics.DestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        queryset = Education.objects.all()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('id'))

        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this object.")

        return obj


class CertificateCreateView(generics.CreateAPIView):
    queryset = Certification.objects.all()
    serializer_class = serializers.CertificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CertificateUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Certification.objects.all()
    serializer_class = serializers.CertificationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        queryset = Certification.objects.all()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('id'))

        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this object.")

        return obj


class CertificateDeleteView(generics.DestroyAPIView):
    queryset = Certification.objects.all()
    serializer_class = serializers.CertificationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        queryset = Certification.objects.all()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('id'))

        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this object.")

        return obj



