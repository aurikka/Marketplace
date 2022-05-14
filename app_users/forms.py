from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(label=_('First name'), max_length=30, required=False)
    last_name = forms.CharField(label=_('Last name'), max_length=40, required=False)
    email = forms.EmailField(label='e-mail')
    city = forms.CharField(label=_('City'), max_length=36, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'city',
                  'password1', 'password2')

