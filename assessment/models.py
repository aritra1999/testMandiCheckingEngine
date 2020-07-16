from django.db import models

class Assessment(models.Model):
    code = models.CharField(max_length=10, null=True, blank=True)
    question_id = models.CharField(max_length=200, null=True, blank=True)
    org = models.CharField(max_length=120, null=True, blank=True)
    time_limit = models.IntegerField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.code)


class AssessmentManager(models.Model):
    assessment_code = models.CharField(max_length=10, null=True, blank=True)
    user = models.CharField(max_length=120, null=True, blank=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    time_taken = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.user)


class AssessmentSubmission(models.Model):
    user = models.CharField(max_length=120, null=True, blank=True)
    assessment_code = models.CharField(max_length=120, null=True, blank=True)
    question_hit = models.CharField(max_length=120, null=True, blank=True)
    solution = models.CharField(max_length=220, null=True, blank=True)
    correctness = models.BooleanField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question_hit)



