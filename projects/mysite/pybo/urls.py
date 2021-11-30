# 위치 참조 관련 라이브러리
from django.urls import path
# . (같은 폴더)의 views.py 파일 import
from . import views

urlpatterns = [
    # path 함수를 사용해 pybo/ URL과 views.index를 매핑
    path('', views.index),
    # path 함수를 사용해 pybo/ URL과 views.detail를 매핑
    path('<int:question_id>/', views.detail),
]