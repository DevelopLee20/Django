# 명령어

## 파일 생성

```cmd
mkdir [파일명]
```

## 파일로 이동

```cmd
cd [폴더명]
```

## 가상환경 생성

```cmd
python -m venv [가상환경 이름]
```

## 가상환경 활성화

```cmd
// 가상환경 진입 후
activate
```

## 가상환경 비활성화

```cmd
// 가상환경 활성화 상태에서
deactivate
```

## 장고 프로젝트 생성

```cmd
django-admin startproject config .
```

## 개발 서버 구동

```cmd
python manage.py runserver
```

## cmd 배치 파일 생성하기

```cmd
@echo off
cd [프로젝트 주소]
가상환경 주소/activate
```

> 위의 작업 후 cmd 배치파일의 위치에 사용자 환경변수 설정

## 앱 생성하기

```cmd
// 가상환경 진입 후
django-admin startapp [앱이름]
```

## 앱에서 사용할 테이블 생성하기

```cmd
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

```cmd
// 개발 서버 구동시에 위의 문장이 출력될 때 해당 코드 사용
python manage.py migrate
```

## 테이블 작업 파일 생성하기

```cmd
Your models in app(s): 'pybo' have changes that are not yet reflected in a migration, and so won't be applied.
Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them
```

```cmd
// migrate 작업이 제대로 수행되지 않을 때 해당 코드 실행
python manage.py makemigrations
```

> 해당 코드 실행시 0000_파일명.py 소스 파일이 생성됨
>
> 코드 실행 후 migrate 실행

## 테이블 작업에서 어떤 쿼리문이 실행되는지 확인

```cmd
python manage.py sqlmigrate [앱이름] [0000]
```

## 장고 셀 실행하기

```cmd
python manage.py shell
```

## 슈퍼 유저 생성(어드민 계정)

```cmd
python manage.py createsuperuser
```

## 템플릿 태그

```html
<!-- // 만약 question_list 가 있다면 -->
{% if question_list %}  
<ul>
    <!-- // question_list 내의 모든 요소를 question에 -->
    {% for question in question_list %} 
    <li><a href="/pybo/{{question.id}}/">{{question.subject}}</a></li>
<!-- // 반복 종료 -->
{% endfor %}    
</ul>
<!-- // if else 문 -->
{% else %}  
<p>질문이 없습니다.</p>
<!-- if 종료 문 -->
{% endif %} 
```

```html
<!-- models.py에 있는 Question 클래스의 subject -->
<h1>{{question.subject}}</h1>
<div>
    <!-- models.py에 있는 Question 클래스의 content -->
    {{question.content}}
</div>
```
