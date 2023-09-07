# 정의된 함수에서 사용할 모듈 HttpResponse를 import
from django.shortcuts import render, HttpResponse
import random

# Create your views here.

# 첫번째 파라미터의 인자로 요청과 관련된 여러가지 정보가 들어오도록 약속되어 있는 객체를 전달해주도록 되어있음
# def index(request):
#     return HttpResponse('<h1>Random</h1>' + str(random.random())) # HttpResponse : http를 통해서 응답하겠다는 의미의 객체

# 글의 내용을 list 형식으로 생성
topics = [
    {'id':1, 'title':'Routing', 'body':'Routing is..'}, # 하나의 글을 dictionary 형식으로 생성
    {'id':2, 'title':'View', 'body':'View is..'},
    {'id':3, 'title':'Model', 'body':'Model is..'},
]

# 간단한 웹 페이지 형식을 출력하도록 생성
def index(request):
    # 위에서 정의한 topics를 함수 내부에서 사용하도록 전역변수로 선언
    global topics
    ol = ''
    for topic in topics:
        # f:format을 사용하여 dictionary 형식의 데이터를 불러옴
        ol += f'''<li>
                    <a href="/read/{topic["id"]}">{topic["title"]}</a>
                </li>'''
    return HttpResponse(f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <br>
        <h2>Welcome</h2>
        Hello, Django
    </body>
    </html>
    ''')

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read' + id)