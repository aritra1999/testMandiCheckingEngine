from django.shortcuts import render
from .models import QuestionCategory,Languagedefault
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
import json
from django.http import JsonResponse
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


def questions_category(request):
    print("zjajaj")
    if request.is_ajax():
        sector = QuestionCategory.objects.filter(levelone=request.GET.get('sector', ''))
        print("hello worl")
        print(sector.values('leveltwo').distinct())
        sector=sector.values('leveltwo').distinct()
        html = render_to_string('metadata/leveltwo.html', locals())
        return HttpResponse(html)
        # print("yolo")
        # for x in sector:
        #     print(x.sub_sectors)

def questions_subcategory(request):
    print("zjajaj")
    if request.is_ajax():
        sector = QuestionCategory.objects.filter(leveltwo=request.GET.get('sector', ''))
        html = render_to_string('metadata/levelthree.html', locals())
        return HttpResponse(html)
        # print("yolo")
        # for x in sector:
        #     print(x.sub_sectors)


def business_sector():
    data = QuestionCategory.objects.values('levelone').distinct()
    return data


def language_default(request):
    if request.is_ajax():
        sector = Languagedefault.objects.get(subvalue=request.GET.get('sector', ''))
        print(request.GET.get('sector', ''))
        print(sector)
        return HttpResponse(sector.default_text)
