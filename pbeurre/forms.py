from django import forms
# from dal import autocomplete
# from pbeurre import models

class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=50)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)


# class FoodForm(forms.ModelForm):
#     class Meta:
#         model = models.Food
#         fields = 'name'
#         widgets = {
#             'name': autocomplete.ModelSelect2(url='food-autocomplete')
#         }