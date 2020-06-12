from django.contrib import admin
from .models import Question, Submission, Input, Output

admin.site.register(Question)
admin.site.register(Submission)
admin.site.register(Input)
admin.site.register(Output)

