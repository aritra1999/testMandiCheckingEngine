from django.contrib import admin
from .models import Question, Submission, MCQQuestion, MCQSolution

admin.site.register(Question)
admin.site.register(Submission)
admin.site.register(MCQQuestion)
admin.site.register(MCQSolution)



