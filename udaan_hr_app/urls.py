"""udaan_hr_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from hr_app import views as hr_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hr_views.home, name='home'),
    path('success',hr_views.success, name='success'),
    path('user/', hr_views.administrator, name='administrator'),
    path('pie-chart/', hr_views.pie_chart, name='pie-chart'),
    path('user/send_email/', hr_views.send_mail, name='send_mail'),
    path('status_change/',hr_views.status_change, name='status_change')
    # url(r'^ajax/change_status/$', hr_views.ajax_change_status, name='ajax_change_status')
    # path('request/<user_id>/', hr_views.request, name='request'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
