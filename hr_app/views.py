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

            # if user_type == "Student":
            #     form.student_count += 1
            # elif user_type == "Employed":
            #     form.employed_count += 1
            # elif user_type == "Unemployed":
            #     form.unemployed_count += 1
            #
            # print(name, email, phone, user_type)
            form.save()
            return redirect('success')

    form = CreateUserInfo()
    return render(request, 'user.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def administrator(request):
    query_results = UserInfo.objects.all()
    context = {'query_result': query_results}
    return render(request, 'admin.html', locals())


def pie_chart(request):
    labels = []
    data = []


    # UserInfo.unemployed_count
    # labels.append('Employed')
    # data.append(queryset1.employed_count)
    # labels.append('Unemployed')
    # data.append(queryset1.unemployed_count)
    # labels.append('Student')
    # # data.append(queryset1.student_count)
    # # print(queryset.student_count)
    print(UserInfo.unemployed_count)
    print((UserInfo.employed_count))

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })


def approve(request):
    return HttpResponse('Approve')
