from pbeurre.models import Food
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.CharField(
        label='Email',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
        )
    password = forms.CharField(
        label="Password",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)
