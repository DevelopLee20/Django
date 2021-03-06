# 페이지 요청에 의한 응답을 할 때 사용하는 클래스
from django.http import HttpResponse
# Question 클래스 참조
from .models import Answer, Question
# 모델 데이터를 HTML로 변환
from django.shortcuts import render
# 존재하지 않는 페이지에 접속했을때 404 Error 출력을 위한 import
from django.shortcuts import get_object_or_404
# 시간 관련 함수가 들어있음
from django.utils import timezone
# 함수에 전달된 값을 참고하여 페이지 이동을 수행한다. (HTML 대신 url을 타고 이동함)
from django.shortcuts import redirect
# QuestionForm: 질문을 등록하기 위해 사용하는 장고의 폼 클래스
from .forms import QuestionForm, AnswerForm

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

def answer_create(request, question_id):
    # question_id가 비정상적으로 반환되면, 404 Error를 출력한다.
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = AnswerForm()
    context = {'question':question, 'form':form}
    return render(request,'pybo/question_detail.html', context)
    
    # answer_set: Question 모델을 통해 Answer 모델 데이터를 생성
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # # HTML 대신 url을 타고 이동함
    # return redirect('pybo:detail', question_id=question_id)

def question_create(request):
    # post 방식일떄
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # commit : 임시저장 여부
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    # get 방식일때
    else:
        form = QuestionForm()            
        # {'form':form} : 템플릿에 폼 화면을 생성
        context = {'form':form}
        return render(request, 'pybo/question_form.html', context)