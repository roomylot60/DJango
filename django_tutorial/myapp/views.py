# 정의된 함수에서 사용할 모듈 HttpResponse를 import
from django.shortcuts import render, HttpResponse, redirect
import random
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# 첫번째 파라미터의 인자로 요청과 관련된 여러가지 정보가 들어오도록 약속되어 있는 객체를 전달해주도록 되어있음
# def index(request):
#     return HttpResponse('<h1>Random</h1>' + str(random.random())) # HttpResponse : http를 통해서 응답하겠다는 의미의 객체

nextId = 4
# 글의 내용을 list 형식으로 생성
topics = [
    {'id':1, 'title':'Routing', 'body':'Routing is..'}, # 하나의 글을 dictionary 형식으로 생성
    {'id':2, 'title':'View', 'body':'View is..'},
    {'id':3, 'title':'Model', 'body':'Model is..'},
]

# 간단한 웹 페이지 형식을 출력하도록 생성
# def index(request):
#     # 위에서 정의한 topics를 함수 내부에서 사용하도록 전역변수로 선언
#     global topics
#     ol = ''
#     for topic in topics:
#         # f:format을 사용하여 dictionary 형식의 데이터를 불러옴
#         ol += f'''<li>
#                     <a href="/read/{topic["id"]}">{topic["title"]}</a>
#                 </li>'''
#     return HttpResponse(f'''
#     <html>
#     <body>
#         <h1>Django</h1>
#         <ol>
#             {ol}
#         </ol>
#         <br>
#         <h2>Welcome</h2>
#         Hello, Django
#     </body>
#     </html>
#     ''')

# 페이지 생성 함수
def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action='/delete/' method='post'>
                    <input type='hidden' name='id' value={id}>
                    <input type='submit' value='delete'>
                </form>
            </li>
            <li><a href="/update/{id}">update</a></li>
        '''
    ol = ''
    for topic in topics:
        # f:format을 사용하여 dictionary 형식의 데이터를 불러옴
        ol += f'''<li>
                    <a href="/read/{topic["id"]}">{topic["title"]}</a>
                </li>'''
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        <br>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
        </ul>
    </body>
    </html>
    '''

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST["title"]
        body = request.POST["body"]
        newTopic = {'id':nextId, 'title':title, 'body':body}
        topics.append(newTopic)
        url = '/read/'+ str(nextId)
        nextId += 1
        return redirect(url)

@csrf_exempt
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                }
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectedTopic['title']}></p>
                <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
    return redirect('/')