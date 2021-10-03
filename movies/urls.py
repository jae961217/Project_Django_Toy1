# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [

    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/edit/', views.edit, name='edit'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),

    # path('movies/', include('movies/urls.py')),
    # path('admin/', admin.site.urls),
]

# /movies/new/
# 새로운 영화 작성 Form
# /movies/create/
# 영화 데이터 저장
# /movies/
# 전체 영화 목록 조회
# /movies/<pk>/
# 단일 영화 상세 조회
# /movies/<pk>/edit/
# 단일 영화 수정 Form
# /movies/<pk>/update/
# 수정된 영화 데이터 저장
# /movies/<pk>/delete/
# 단일 영화 삭제

