from django.contrib import admin
from .models import Assessment, AssessmentManager, AssessmentSubmission

admin.site.register(Assessment)
admin.site.register(AssessmentManager)
admin.site.register(AssessmentSubmission)


