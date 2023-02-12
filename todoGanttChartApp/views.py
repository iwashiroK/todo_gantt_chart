from django.shortcuts import render
from .models import CATEGORIES


# Create your views here.
#追加
def displayCategoryfunction(request):
    return render(request, 'index.html')

def registCategoryfunction(request):
    qs = CATEGORIES.objects.all()
    params = {
        "val" : qs,
        }
    
    return render(request, 'regist_category.html', params)
