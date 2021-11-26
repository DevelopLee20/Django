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
from django.urls import path
# 화면을 보여주기 위한 views 함수 불러오기
from pybo import views

# URL 매핑을 추가하는 부분
# URL 끝에는 / 를 붙이는 것이 일반적이다.
urlpatterns = [
    path('admin/', admin.site.urls),
    # pybo라는 URL 주소를 추가 index 함수를 화면에 보여줌
    # path 함수를 사용해 pybo/ URL과 views.index를 매핑
    path('pybo/', views.index),
]
