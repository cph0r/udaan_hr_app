from django.forms import ModelForm
from django_tables2 import TemplateColumn

from .models import UserInfo


class CreateUserInfo(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'email','phone','photo', 'type']
