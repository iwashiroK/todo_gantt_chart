from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class CATEGORIES(models.Model):
    CATEGORY_ID = models.CharField(max_length=5,primary_key=True)
    #models.ForeignKey('auth.User', on_delete=models.CASCADE)
    CATEGORY_NAME = models.CharField(max_length=20)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title