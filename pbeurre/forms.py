from django import forms
from dal import autocomplete
from pbeurre.models import Food
from django.utils.html import format_html


class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=50)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)


class FoodForm(forms.ModelForm):
    class Meta:
        widgets = {
            'name': autocomplete.ModelSelect2(
                url='food-autocomplete',
                attrs={'data-html': True}
            )
        }