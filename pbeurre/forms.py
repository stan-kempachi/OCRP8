from django import forms
from dal import autocomplete

from pbeurre.models import Food
from django.utils.html import format_html

from django_select2.forms import Select2MultipleWidget
from django import forms
from dal import autocomplete


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


# autocomplete.ModelSelect2(Food,
#     # Just like in ModelAdmin.search_fields.
#     # search_fields=['name', 'categorie_tag1'],
#     attrs={
#         # This will set the input placeholder attribute:
#         'placeholder': 'query',
#         # This will set the yourlabs.Autocomplete.minimumCharacters
#         # options, the naming conversion is handled by jQuery.
#         'data-autocomplete-minimum-characters': 1,
#     },
#     # This will set the data-widget-maximum-values attribute on the
#     # widget container element, and will be set to
#     # yourlabs.Widget.maximumValues (jQuery handles the naming
#     # conversion).
#     widget_attrs={
#         'data-widget-maximum-values': 6,
#         # Enable modern-style widget !
#         'class': 'modern-style',
#     },
# )

class FoodForm(forms.Form):
    class Meta:
        model = Food
        fields = ('name')
        widgets = {
            'name': autocomplete.ModelSelect2(url='pbeurre:food-autocomplete')
        }