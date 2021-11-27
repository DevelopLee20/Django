from django.db import models

# 질문을 받을 클래스 선언
class Question(models.Model):
    # 문자열필드 생성, 최대 글자수 200
    subject = models.CharField(max_length=200)
    # 글자수가 제한 없는 텍스트 필드
    content = models.TextField()
    # 날짜, 시간 관련 속성 필드 
    create_date = models.DateTimeField()

    # __str__ 클래스 자체 내용을 출력하고 싶을때 형식 지정
    def __str__(self):
        # subject의 str를 반환한다.
        return self.subject

# 답변을 할 클래스 선언
class Answer(models.Model):
    # ForeignKey : 다른 모델간의 연결, on_delete 관련된 질문과 삭제시 같이 삭제됨
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 글자수가 제한 없는 텍스트 필드
    content = models.TextField()
    # 날짜, 시간 관련 속성 필드
    create_date = models.DateTimeField()