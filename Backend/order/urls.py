from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create-order/', views.OrderCreateView.as_view(), name='create-order'),
    path('update-order/<int:pk>/', views.OrderUpdateView.as_view(), name='update-order'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)