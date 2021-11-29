# 페이지 요청에 의한 응답을 할 때 사용하는 클래스
from django.http import HttpResponse
# Question 클래스 참조
from .models import Question
# 모델 데이터를 HTML로 변환
from django.shortcuts import render

def index(request):
    # order_by : 특정 속성 기준으로 특정 속성을 정렬, create_date: 작성일시, -create_date: 작성일시 역순
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)