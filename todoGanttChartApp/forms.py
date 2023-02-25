from django import forms 
from .models import CATEGORIES

class CATEGORIESFORM(forms.ModelForm):
    class Meta:
        model = CATEGORIES
        fields = ('CATEGORY_NAME',)
        labels = {'CATEGORY_NAME':'カテゴリ名'}