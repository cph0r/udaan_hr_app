from django.shortcuts import render, redirect
from django.http import HttpResponse
from .user_form import UserForms
from .models import UserInfo
from .forms import CreateUserInfo


# Create your views here.


def home(request):
    if request.method == "POST":
        form = CreateUserInfo(request.POST, request.FILES)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            photo = form.cleaned_data['photo']
            user_type = form.cleaned_data['type']
            # print(name, email, phone, user_type)
            form.save()
            return redirect('success')

    form = CreateUserInfo()
    return render(request, 'user.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def admin(request):
    return HttpResponse('Admin')


def approve(request):
    return HttpResponse('Approve')

