"""dj20190528_01_dev_776 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url('', include('home.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/v1/', include('home.api.v1.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'dj20190528-01'
admin.site.site_title = 'dj20190528-01 Admin Portal'
admin.site.index_title = 'dj20190528-01 Admin'
