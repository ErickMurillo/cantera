from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(required=True,label='Correo electrónico')

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    email = forms.CharField(required=True,label='Correo electrónico')
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar',)

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'avatar',)
        exclude = ('password',)