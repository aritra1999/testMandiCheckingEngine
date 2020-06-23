from django.contrib import admin
from .models import Question, Submission, IO

admin.site.register(Question)
admin.site.register(Submission)
admin.site.register(IO)

