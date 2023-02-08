"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from pybo import views
from main import views

#ex) path('main/', include('main.urls')), 메인에있는 폴더의 url을 가져오겟다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('', include('main.urls')),
    path('common/', include('common.urls')),
    path('main/', include('main.urls')),
    path('', views.main, name='main'),
    path('v1/', include('v1.urls')),
    path('product/', views.product, name='product'),
    path('contentform/', views.contentform, name='contentform'),
    path('price/', views.price, name='price'),
]


