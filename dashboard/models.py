from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    question = models.TextField(max_length=5000, blank=True, null=True)
    hit = models.CharField(max_length=10, blank=True, null=True)
    time_limit = models.CharField(max_length=10, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Submission(models.Model):
    user = models.CharField(max_length=120, blank=True, null=True)
    question_hit = models.CharField(max_length=10, blank=True, null=True)
    time_taken = models.CharField(max_length=10, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    solution = models.TextField(max_length=100000, blank=True, null=True)
    verdict = models.BooleanField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user + " | " + self.question_hit)


class Input(models.Model):
    question_hit = models.CharField(max_length=10, blank=True, null=True)
    input_number = models.IntegerField(blank=True, null=True)
    input = models.TextField(max_length=10000, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_hit


class Output(models.Model):
    question_hit = models.CharField(max_length=10, blank=True, null=True)
    output_number = models.IntegerField(blank=True, null=True)
    output = models.TextField(max_length=10000, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_hit