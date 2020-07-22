from django.contrib import admin
from .models import StudentProfile, OrgProfile, OTPLog

admin.site.register(StudentProfile)
admin.site.register(OrgProfile)
admin.site.register(OTPLog)



