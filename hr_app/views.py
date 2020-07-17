from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .user_form import UserForms
from .models import UserInfo
from .forms import CreateUserInfo
from django.core.mail import send_mail


# Create your views here.
def home(request):
    if request.method == "POST":
        form = CreateUserInfo(request.POST, request.FILES)
        data = UserInfo()
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            photo = form.cleaned_data['photo']
            user_type = form.cleaned_data['type']

            print(name, email, phone, user_type)
            data.name = name
            data.phone = phone
            data.type = user_type
            data.photo = photo
            data.email = email
            data.save()
            return redirect('success')

    form = CreateUserInfo()
    return render(request, 'user.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def administrator(request):
    query_results = UserInfo.objects.all()
    context = {'query_result': query_results}
    return render(request, 'admin.html', locals())


def status_change(request):
    if request.method == 'POST':
        # First, you should retrieve the team instance you want to update
        print(request.POST.get('user_id'))
        print(request.POST.get('status'))
        user = UserInfo.objects.get(user_id=request.POST.get('user_id'))

        # Next, you update the status
        if request.POST.get('status'):
            user.status = request.POST.get('status')
            user.save()

    return HttpResponse('success')


# def ajax_change_status(request):
#     approve_request = request.GET.get('status', False)
#     user_id = request.GET.get('user_id', False)
#     # first you get your Job model
#     user = UserInfo.objects.get(pk=user_id)
#     try:
#         user.status = approve_request
#         user.save()
#         return JsonResponse({"success": True})
#     except Exception as e:
#         return JsonResponse({"success": False})
#     return JsonResponse(data)


def pie_chart(request):
    labels = []
    data = []

    all_data = UserInfo.objects.all()
    count1 = 0
    count2 = 0
    count3 = 0

    for items in all_data:
        if items.type == 'Student':
            count1 += 1
        elif items.type == 'Employed':
            count2 += 1
        elif items.type == 'Unemployed':
            count3 += 1

    UserInfo.unemployed_count
    labels.append('Employed')
    data.append(count2)
    labels.append('Unemployed')
    data.append(count3)
    labels.append('Student')
    data.append(count1)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })


def send_email(request):
    send_mail(subject='Request Approval',
              message='Your request has been approved',
              from_email='chirag.phor2016@vitstudent.ac.in',
              recipient_list=['dilok52717@pastmao.com'],
              fail_silently=False,
              )

    return HttpResponse('confirmation mail sent')


def approve(request):
    return HttpResponse('Approve')
