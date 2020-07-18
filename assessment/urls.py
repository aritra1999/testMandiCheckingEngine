from django.urls import path, include

from .views import assessment_home_view, assessment_view, assessment_success_view

urlpatterns = [
    path('', assessment_home_view, name="assesment-home"),
    path('success/', assessment_success_view, name="assesment-success"),
    path('<assessment_code>/', assessment_view, name="assessment"),
    # path('<assessment_code>/<hit>', assessment_question_view, name="assessment-question")
]