from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Assessment
from dashboard.models import Question, MCQQuestion

@login_required
def assessment_home_view(request):
    context = {
        'title': 'Assessment Home'
    }
    if request.method == "POST":
        assessment_code = request.POST.get("assessment")

        assessment = Assessment.objects.filter(code=assessment_code)
        if assessment.count() == 0:
            context['error'] = "Invalid Assessment code."
        else:
            return redirect(assessment_code + "/")
    return render(request, "assessment/home.html", context)

@login_required
def assessment_view(request, assessment_code):
    try:
        assessment = Assessment.objects.get(code=assessment_code)
    except:
        return redirect("/assessment/")
    questions = assessment.question_id.split(',')

    context = {
        'title': assessment_code,
        'assessment': assessment,
        'questions': questions
    }

    return render(request, 'assessment/assessment.html', context)
