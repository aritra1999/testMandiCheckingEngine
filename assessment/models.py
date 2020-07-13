from django.db import models

class Assessment(models.Model):
    code = models.CharField(max_length=10, null=True, blank=True)
    question_id = models.CharField(max_length=200, null=True, blank=True)
    org = models.CharField(max_length=120, null=True, blank=True)
    time_limit = models.IntegerField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.code)

