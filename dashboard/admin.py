from django.contrib import admin
from .models import Question, Submission, IO, MCQQuestion, MCQSolution

admin.site.register(Question)
admin.site.register(Submission)
admin.site.register(IO)
admin.site.register(MCQQuestion)
admin.site.register(MCQSolution)



