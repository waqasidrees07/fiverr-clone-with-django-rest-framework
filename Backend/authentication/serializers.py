from rest_framework import serializers
from .models import MyUser
import random
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


def generate_verification_code():
    return random.randint(100000, 999999)


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["email", "username", "password"]

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            verification_code=generate_verification_code()
        )
        user.save()

        html_message = render_to_string('email_template.html',
                                        {"username": user.username, "verification_code": user.verification_code})
        plain_message = strip_tags(render_to_string('email_template.txt'))
        mail = EmailMultiAlternatives(
            f'Account Verification',
            f'{plain_message}',
            'waqasidrees15@gmail.com',
            [f'{user.email}'],
        )
        mail.attach_alternative(html_message, "text/html")
        mail.send()

        return user


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username']


class EmailVerificationSerializer(serializers.Serializer):
    verification_code = serializers.CharField(max_length=6, required=True)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

    def validate(self, attrs):
        new_password = attrs.get("new_password")
        confirm_new_password = attrs.get("confirm_new_password")

        if new_password != confirm_new_password:
            raise serializers.ValidationError("New passwords must match.")

        return attrs


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

    def validate(self, attrs):
        new_password = attrs.get("new_password")
        confirm_new_password = attrs.get("confirm_new_password")

        if new_password != confirm_new_password:
            raise serializers.ValidationError("New passwords must match.")

        return attrs
