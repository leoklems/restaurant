from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Select, TextInput, CheckboxInput, CheckboxSelectMultiple
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exists():
            raise ValidationError({'email': 'Email Already Exists'})
        if User.objects.filter(username=username).exists():
            raise ValidationError({'username': 'Username Already Exists'})    
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:

        widgets = {
             'password': TextInput(attrs={
                 'class': 'form-control',
                 'type': 'password',
             }),

        }

