from django import forms
from .models import Gig, BasicPackage, StandardPackage, PremiumPackage


class GigForm(forms.ModelForm):
    gig_title = forms.TextInput(attrs={"class": "form-control"})
