from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^question_category', views.questions_category, name="questions_category"),  
    re_path(r'^question_subcategory', views.questions_subcategory, name="questions_subcategory"), 
    re_path(r'^language_default', views.language_default, name="language_default"), 
]
