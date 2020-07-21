from django.db import models
from datetime import datetime

# Create your models here.
class QuestionCategory(models.Model):
    levelone = models.CharField(max_length=255, blank= True, default = "")
    leveltwo = models.CharField(max_length=255, blank= True, default = "")
    levelthree = models.CharField(max_length=255, blank= True, default = "")


class Languagedefault(models.Model):
    language = models.CharField(max_length=255, blank= True, default = "")
    version = models.CharField(max_length=255, blank= True, default = "")
    default_text = models.TextField(max_length=5000, blank=True, null=True)
    value = models.CharField(max_length=255, blank= True, default = "")
    subvalue = models.CharField(max_length=255, blank= True, default = "")