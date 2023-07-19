from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('user/profile/', views.UserProfileView.as_view(), name="user-profile"),
    path('update-profile/', views.MyUserProfileUpdateView.as_view(), name='update-profile'),
    path('create-language/', views.LanguageCreateView.as_view(), name='create-language'),
    path('update-language/<int:id>', views.LanguageUpdateView.as_view(), name='update-language'),
    path('delete-language/<int:id>', views.LanguageDeleteView.as_view(), name='delete-language'),
    path('create-skill/', views.SkillCreateView.as_view(), name='create-skill'),
    path('update-skill/<int:id>', views.SkillUpdateView.as_view(), name='update-skill'),
    path('delete-skill/<int:id>', views.SkillDeleteView.as_view(), name='delete-skill'),
    path('create-education/', views.EducationCreateView.as_view(), name='create-education'),
    path('update-education/<int:id>', views.EducationUpdateView.as_view(), name='update-education'),
    path('delete-education/<int:id>', views.EducationDeleteView.as_view(), name='delete-education'),
    path('create-certificate/', views.CertificateCreateView.as_view(), name='create-certificate'),
    path('update-certificate/<int:id>', views.CertificateUpdateView.as_view(), name='update-certificate'),
    path('delete-certificate/<int:id>', views.CertificateDeleteView.as_view(), name='delete-certificate'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
