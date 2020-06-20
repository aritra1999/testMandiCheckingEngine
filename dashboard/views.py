from django.conf import settings
from django.shortcuts import render
from .models import Question, Submission, Output, Input

from .utils import code_checker

def dashboard_view(request):
    context = {
        "title": "Dashboard"
    }
    return render(request, 'dashboard/dashboard.html', context)


def question_list_view(request):
    questions = Question.objects.all()
    context = {
        "title": "Dashboard",
        "questions": questions
    }

    return render(request, 'dashboard/question-list.html', context)


def question_details_view(request, hit):
    question = Question.objects.get(hit=hit)
    context = {
        "title": hit,
        "question": question
    }

    user = "test-user"

    if request.method == "POST":
        question_hit = hit
        solution = request.POST.get('solution')
        language = request.POST.get('language')

        time_taken, verdict = code_checker(request, solution, language, question_hit, username="test-user")

        if verdict == "error":
            context["error"] = "There's some error in your code. Please check and retry."
            context["code"] = solution
            context["language"] = language

            return render(request, 'dashboard/question.html', context)
        else:
            if verdict == True:context["result"] = "Correct Answer"
            else: context["result"] = "Wrong Answer"

            context["time_taken"] = round(time_taken, 2)
            Submission.objects.create(user=user, question_hit=question_hit, time_taken=time_taken, verdict=verdict, solution=solution, language=language).save()

    code = Submission.objects.filter(user=user, question_hit=hit).order_by('-time_stamp')
    if code.count() > 0:
        context["code"] = code.first().solution
        context["language"] = code.first().language
    else:
        context["code"] = ""
        context["language"] = "c_cpp"

    return render(request, 'dashboard/question.html', context)


def submissions_view(request):
    user = "test-user"
    context = {
        "title": "Submissions",
        "submissions": Submission.objects.filter(user=user).order_by('-time_stamp')
    }

    return render(request, "dashboard/submissions.html", context)


