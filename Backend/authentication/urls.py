from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path("signup/", views.SignUpView.as_view(), name="signup"),
                  path("email-verification/", views.EmailVerificationView.as_view(), name="email-verification"),
                  path("accounts/login/", views.LoginView.as_view(), name="login"),
                  path("logout/", auth_views.LogoutView.as_view(), name="logout"),
                  path('change-password/', views.PasswordChangeView.as_view(), name='change-password'),
                  path('api/forgot-password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
                  path('api/reset-password/<str:uid>/<str:token>/', views.ResetPasswordView.as_view(),
                       name='reset-password'),
                  path("", views.HomeView.as_view(), name="home"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
