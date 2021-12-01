# 페이지 요청에 의한 응답을 할 때 사용하는 클래스
from django.http import HttpResponse
# Question 클래스 참조
from .models import Question
# 모델 데이터를 HTML로 변환
from django.shortcuts import render
# 존재하지 않는 페이지에 접속했을때 404 Error 출력을 위한 import
from django.shortcuts import get_object_or_404

def index(request):
    # order_by : 특정 속성 기준으로 특정 속성을 정렬, create_date: 작성일시, -create_date: 작성일시 역순
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # id = question_id 변수에서 불러와 get으로 특정 데이터를 가져온다.
    # question = Question.objects.get(id=question_id)
    # Question에서 pk에 해당하는 건이 없어서 반환이 비정상하면, 404 페이지를 출력한다.
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    # 질문을 context를 html에 적용한 후 HTML 코드로 변환한다.
    return render(request, 'pybo/question_detail.html', context)