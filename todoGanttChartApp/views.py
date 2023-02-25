from django.shortcuts import render
from .models import CATEGORIES
from django import forms
from .forms import CATEGORIESFORM

# Create your views here.
#初期画面へ遷移する
def displayCategoryfunction(request):
    return render(request, 'index.html')

#カテゴリ一覧表示および登録画面へ遷移する
def registCategoryfunction(request):
    qs = CATEGORIES.objects.all()
    form = CATEGORIESFORM()
    params = {
        "val" : qs,
        "form" : form,
        }
    return render(request, 'regist_category.html', params)

# フォームから受取ったデータをDBに登録する
def addCategory(request):
    #リクエストがPOSTの場合
    if request.method == 'POST':
        #リクエストをもとにフォームをインスタンス化
        cateogriesForm = CATEGORIESFORM(request.POST)
        if cateogriesForm.is_valid():
            cateogriesForm.save()
 
    #登録後、全件データを抽出
    categories = CATEGORIES.objects.all()
    qs = CATEGORIES.objects.all()
    params = {
        "val" : qs,
        }
    return render(request, 'regist_category.html', params)