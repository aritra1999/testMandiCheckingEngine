from django.db import models

QUESTION_DIFFI = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10")
)


class Question(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    question = models.TextField(max_length=5000, blank=True, null=True)
    hit = models.CharField(max_length=10, blank=True, null=True)
    difficulty = models.IntegerField(choices=QUESTION_DIFFI, blank=True, null=True)
    topic = models.CharField(max_length=250, blank=True, null=True)
    subtopic = models.CharField(max_length=250, blank=True, null=True)
    subsubtopic = models.CharField(max_length=250, blank=True, null=True)
    time_limit = models.CharField(max_length=10, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MCQQuestion(models.Model):
    question = models.TextField(max_length=5000, blank=True, null=True)
    hit = models.CharField(max_length=10, blank=True, null=True)
    difficulty = models.IntegerField(choices=QUESTION_DIFFI, blank=True, null=True)
    topic = models.CharField(max_length=250, blank=True, null=True)
    subtopic = models.CharField(max_length=250, blank=True, null=True)
    subsubtopic = models.CharField(max_length=250, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question)


class MCQSolution(models.Model):
    question_hit = models.CharField(max_length=10, blank=True, null=True)
    solution = models.CharField(max_length=120, blank=True, null=True)
    correctness = models.BooleanField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.solution)


class Submission(models.Model):
    user = models.CharField(max_length=120, blank=True, null=True)
    question_hit = models.CharField(max_length=10, blank=True, null=True)
    time_taken = models.CharField(max_length=10, blank=True, null=True)
    space_taken = models.CharField(max_length=10, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    solution = models.TextField(max_length=100000, blank=True, null=True)
    verdict = models.BooleanField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user + " | " + self.question_hit)


