from django import forms
from .models import user, Business,neighbourhood

class accounts(forms.ModelForm):
    class Meta:
        model= user
        exclude = ['user','Neighbourhood']

class businessaccount(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner', 'Neighbourhood']

