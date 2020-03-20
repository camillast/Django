from django import forms
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
