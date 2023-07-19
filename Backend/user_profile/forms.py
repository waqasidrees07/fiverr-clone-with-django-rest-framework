from django import forms
from .models import MyUserProfile


class MyUserProfileForm(forms.ModelForm):
    class Meta:
        model = MyUserProfile
        fields = ['full_name', 'profile_picture', 'description', 'country']
