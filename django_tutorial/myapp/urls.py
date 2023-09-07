from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index), # 해당 경로로 접속되었을 때, 위에서 import 한 모듈 views에 존재하는 함수 index를 실행
    path('create/', views.create), 
    path('read/<id>/', views.read) # tag를 통해 변수(현재 변수명은 id)를 설정가능
]
