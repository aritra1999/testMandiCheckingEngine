from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include,re_path

from dashboard.views import question_list_view, question_details_view, submissions_view, dashboard_view, staff_view, \
                            add_code_question_view,update_code_question_view, add_mcq_question_view, add_mcq_solution_view,delete_code_question_view,question_validate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', staff_view, name='staff'),
    path('staff/add_code_question/', add_code_question_view, name='add-code-question'),
    path('staff/update_code_question/<str:hit>', update_code_question_view, name='update-code-question'),
    path('staff/delete_code_question/<str:hit>', delete_code_question_view, name='delete-code-question'),
    path('staff/add_mcq_question/', add_mcq_question_view, name='add-mcq-question'),
    path('staff/add_mcq_solution/<hit>', add_mcq_solution_view, name='add-mcq-solution'),
    path('', dashboard_view, name="dashboard"),
    path('question/', question_list_view, name="question-list"),
    path('question/<str:hit>', question_details_view, name="question"),
    path('question_validate/<str:hit>', question_validate, name="question_validate"),
    path('submissions/', submissions_view, name="submissions"),
    path('auth/', include('users.urls'), name='auth'),
    path('assessment/', include('assessment.urls'), name='assessment'),
    # path('profile/', include('profile.urls'), name='profile'),
    re_path(r'^metadata/', include(('metadata.urls', 'metadata'), namespace='metadata')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)