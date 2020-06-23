from django.urls import path, include
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import auth_view

urlpatterns = [
    path('', auth_view, name="reglogin"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('reset_password/', PasswordResetView.as_view(), name="reset_password"),
    path('reset_pass_sent/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_pass_complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
