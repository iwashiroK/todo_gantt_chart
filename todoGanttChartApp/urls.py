from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayCategoryfunction),
    path('regist_category.html', views.registCategoryfunction),
]