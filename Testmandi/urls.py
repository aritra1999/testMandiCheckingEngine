from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from dashboard.views import question_list_view, question_details_view, submissions_view, dashboard_view, staff_view, add_question_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', staff_view, name='staff'),
    path('staff/add/', add_question_view, name='add-question'),
    path('', dashboard_view, name="dashboard"),
    path('question/', question_list_view, name="question-list"),
    path('question/<str:hit>', question_details_view, name="question"),
    path('submissions/', submissions_view, name="submissions"),
    path('auth/', include('users.urls'), name='auth')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)