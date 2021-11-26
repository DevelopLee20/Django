from django.shortcuts import render
# 페이지 요청에 의한 응답을 할 때 사용하는 클래스
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")