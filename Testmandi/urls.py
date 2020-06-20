"""Testmandi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from dashboard.views import question_list_view, question_details_view, submissions_view, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name="dashboard"),
    path('question/', question_list_view, name="question-list"),
    path('question/<str:hit>', question_details_view, name="question"),
    path('submissions/', submissions_view, name="submissions"),
    path('auth/', include('users.urls'), name='auth')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)