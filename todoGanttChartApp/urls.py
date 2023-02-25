from django.urls import path
from . import views

urlpatterns = [
    #初期画面へ遷移する
    path('', views.displayCategoryfunction),
    #カテゴリ一覧表示および登録画面へ遷移する
    path('regist_category.html', views.registCategoryfunction),
    #カテゴリ登録する処理を呼び出す
    path('add', views.addCategory, name='addCategory'),
]