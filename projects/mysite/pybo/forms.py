from django import forms
from django.forms import widgets
from pybo.models import Question

# 필수로 Meta 클래스를 가져야한다
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # 필드로 subject와 content를 사용한다고 선언
        fields = ['subject','content']
        # 위젯 설정(정적생성)
        # widgets = {
        #     'subject' : forms.TextInput(attrs={'class':'form-control'}),
        #     'content' : forms.Textarea(attrs={'class':'form-control', 'rows':10}),
        # }
        # 타이틀 한글 관련 설정
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }