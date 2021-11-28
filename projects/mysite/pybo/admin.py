from django.contrib import admin
# Question 함수를 import
from .models import Question

# subject를 검색할 수 있는 클래스
class QuestionAdmin(admin.ModelAdmin):
    # 딕셔너리의 key를 바꾸면, 그에 따라서 검색해서 찾는 내용이 바뀐다
    # search_fields = ['content'] # 이건 내용을 검색해서 찾음
    search_fields = ['subject']

# Question 모델을 장고 Admin에 등록 + ['subject'] 검색할 수 있도록 한다.
admin.site.register(Question, QuestionAdmin)