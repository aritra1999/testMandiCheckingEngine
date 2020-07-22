from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=256, blank=True, null=True)
    headline = models.CharField(max_length=255, blank=True, null=True)
    about_me = models.CharField(max_length=1000, blank=True, null=True)
    user_type = models.CharField(max_length=256, blank=True, null=True)
    website = models.CharField(max_length=256, blank=True, null=True)
    social_website = models.CharField(max_length=256, blank=True, null=True)
    years_exp = models.CharField(max_length=256, blank=True, null=True)
    job_open = models.CharField(default="Yes",max_length=256, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.contact_number)

class OrgProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=120, blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=256, blank=True, null=True)
    website = models.CharField(max_length=256, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.contact_number)


class OTPLog(models.Model):
    email = models.EmailField(blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.otp)