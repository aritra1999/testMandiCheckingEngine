from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import auth_view

urlpatterns = [
    path('', auth_view, name="reglogin"),
    path('logout', LogoutView.as_view(), name="logout")
]
