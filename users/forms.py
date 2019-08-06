from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from organizaciones.models import *

class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(required=True,label='Correo electrónico')

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email','organizacion')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        particular = Contraparte.objects.get(nombre = 'Particular')
        self.fields['organizacion'].initial = particular.id
        self.fields['organizacion'].widget = forms.HiddenInput()

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