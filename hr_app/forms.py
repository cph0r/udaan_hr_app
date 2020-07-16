from django.forms import ModelForm

from .models import UserInfo


class CreateUserInfo(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'email','phone','photo', 'type']