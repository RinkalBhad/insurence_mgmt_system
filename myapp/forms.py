from django import forms
from .models import*

class usersignupform(forms.ModelForm):
    class Meta:
        model=usesignup
        fields='__all__'

class Questionform(forms.ModelForm):
    class Meta:
        model=questiondata
        fields=['description']