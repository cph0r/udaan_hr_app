from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserInfo
from .forms import CreateUserInfo
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        form = CreateUserInfo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')

    form = CreateUserInfo()
    return render(request, 'user.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def administrator(request):
    user_filter = request.GET.get('filter')
    query_results = None
    if user_filter is None or user_filter == '':
        query_results = UserInfo.objects.all()
    else:
        query_results = UserInfo.objects.filter(status=user_filter)
    context = {'query_result': query_results}
    return render(request, 'admin.html', locals())


def status_change(request):
    if request.method == 'POST':
        user = UserInfo.objects.get(user_id=request.POST.get('user_id'))

        if request.POST.get('status'):
            user.status = request.POST.get('status')
            user.save()

    return HttpResponse('success')


def pie_chart(request):
    labels = []
    data = []

    all_data = UserInfo.objects.all()
    count1 = 0
    count2 = 0
    count3 = 0

    for items in all_data:
        if items.status == 'approve':
            count1 += 1
        elif items.status == 'Pending':
            count2 += 1
        elif items.status == 'reject':
            count3 += 1

    labels.append('Pending')
    data.append(count2)
    labels.append('Rejected')
    data.append(count3)
    labels.append('Confirmed')
    data.append(count1)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })


def send_email(request):
    if request.method == 'GET':
        recipient = request.GET.get("email")
        status = request.GET.get('status')
        message = "Unable to get status"
        if status == "approve":
            message = "Your request has been approved"
        elif status == "reject":
            message = "Your request has been rejected"
        send_mail(subject="Request Result",
                  message=message,
                  from_email="chirag.phor2016@vitstudent.ac.in",
                  recipient_list=[recipient],
                  fail_silently=False,
                  )
        return HttpResponse('confirmation mail sent')
    return HttpResponse('confirmation mail was not sent')
