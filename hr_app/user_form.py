from django import forms
from django.db import models


class UserForms(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(max_length=10, min_length=10)
    photo = forms.ImageField()
    type = forms.ChoiceField(choices=[('Employed', 'employed'), ('Unemployed', 'unemployed'), ('Student', 'student')])
