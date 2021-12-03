# 위치 참조 관련 라이브러리
from django.urls import path
# . (같은 폴더)의 views.py 파일 import
from . import views

# app_name : namespace 설정
# namespace : 앱이 관리하는 독립된 이름 공간
app_name = 'pybo'

urlpatterns = [
    # path 함수를 사용해 pybo/ URL과 views.index를 매핑
    # name='index', index를 URL 별칭으로 사용
    path('', views.index, name='index'),
    # path 함수를 사용해 pybo/ URL과 views.detail를 매핑
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]