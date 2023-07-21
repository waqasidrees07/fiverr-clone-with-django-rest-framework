from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("create-gig/", views.GigCreateView.as_view(), name='create-gig'),
    path('user/gigs/', views.GetUserGigsView.as_view(), name='user-gigs'),
    path('gig/<int:id>', views.GetGigView.as_view(), name='get-gig'),
    path('update-gig/<int:id>/', views.GigUpdateView.as_view(), name='update-gig'),
    path('delete-gig/<int:id>/', views.GigDeleteView.as_view(), name='delete-gig'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
