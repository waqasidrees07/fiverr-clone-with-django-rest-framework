from django.shortcuts import redirect
from rest_framework.views import APIView
from .models import MyUser
from rest_framework.response import Response
import random
from user_profile.models import MyUserProfile
from . import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from rest_framework.exceptions import NotFound


class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        user = {"name": "Waqas Ansari"}
        return Response(user)


def generate_verification_code():
    return random.randint(100000, 999999)


class SignUpView(APIView):
    serializer_class = serializers.SignupSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return Response()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"details": "Signup Successfully... Verification Code send to your email"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailVerificationView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.EmailVerificationSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.email_verified:
            return redirect('home')
        return Response()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = self.request.user.email
            verification_code = serializer.validated_data["verification_code"]
            try:
                user = MyUser.objects.get(email=email)
            except MyUser.DoesNotExist:
                return Response({"details": "Invalid Email"})

            if user.verification_code == verification_code:
                user.email_verified = True
                user.save()
                MyUserProfile(user=user).save()
                return Response({"details": "Email Verified Successfully", "user": request.user.username})
            else:
                return Response({"details": "Invalid Verification Code"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = authenticate(email=email, password=password)
            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"details": "Login Successfully", "token": token.key})
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeView(generics.UpdateAPIView):
    serializer_class = serializers.PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Verify the current password
        if not user.check_password(serializer.data.get("current_password")):
            return Response({"current_password": ["Incorrect password."]}, status=status.HTTP_400_BAD_REQUEST)

        # Set the new password
        user.set_password(serializer.data.get("new_password"))
        user.save()

        return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)


class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = serializers.ForgotPasswordSerializer

    def get(self, request):
        user = self.request.user
        if user.is_authenticated:
            return redirect("home")
        return Response()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.data['email']
        try:
            user = MyUser.objects.get(email=email)
        except MyUser.DoesNotExist:
            raise NotFound("Invalid email")

        # Generate the reset password token
        token_generator = default_token_generator
        uid = urlsafe_base64_encode(str(user.pk).encode())
        token = token_generator.make_token(user)

        # Build the reset password email
        reset_url = f"{request.scheme}://{request.get_host()}/api/reset-password/{uid}/{token}/"
        email_subject = 'Password Reset Request'
        email_body = render_to_string('reset_password_email.html', {'reset_url': reset_url})
        email = EmailMessage(subject=email_subject, body=email_body, to=[user.email])
        email.content_subtype = "html"
        email.send()

        return Response({
                            'message': 'we have sent an email with instructions to reset your password.'},
                        status=status.HTTP_200_OK)


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = serializers.ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uid')
        token = kwargs.get('token')
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = MyUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            # Set the new password
            user.set_password(serializer.data['new_password'])
            user.save()

            return Response({'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid reset link or token.'}, status=status.HTTP_400_BAD_REQUEST)
