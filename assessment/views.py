from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import datetime, time

from .models import Assessment, AssessmentManager
from dashboard.models import Question, MCQQuestion, MCQSolution

@login_required
def assessment_home_view(request):
    context = {
        'title': 'Assessment Home'
    }
    if request.method == "POST":
        assessment_code = request.POST.get("assessment")
        try:
            assessment = Assessment.objects.get(code=assessment_code)
        except:
            context['error'] = "Invalid Assessment code."
            return render(request, "assessment/home.html", context)

        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=assessment.time_limit)

        if not AssessmentManager.objects.filter(assessment_code=assessment_code, user=request.user).exists():
            AssessmentManager.objects.create(
                assessment_code=assessment_code,
                user=request.user.username,
                start_time=start_time,
                end_time=end_time
            ).save()

        return redirect(assessment_code + "/")

    return render(request, "assessment/home.html", context)

@login_required
def assessment_view(request, assessment_code):
    try:
        assessment = Assessment.objects.get(code=assessment_code)
    except:
        return redirect("/assessment/")

    questions = []
    mcqquestions = []
    mcqsolutions = []
    hits = assessment.question_id.split(',')


    for hit in hits:
        try:
            questions.append(Question.objects.get(hit=hit))
        except:
            continue

    for hit in hits:
        try:
            mcqquestions.append(MCQQuestion.objects.get(hit=hit))
        except:
            continue

    for hit in hits:
        instances = MCQSolution.objects.filter(question_hit=hit)
        for instance in instances:
            mcqsolutions.append(instance)

    manager = AssessmentManager.objects.get(assessment_code=assessment_code, user=request.user)

    print(manager.end_time)
    print(datetime.datetime.now())

    rem_time = int(time.mktime(manager.end_time.timetuple())) * 1000 - int(time.mktime(datetime.datetime.now().timetuple())) * 1000
    warning_time = manager.end_time - datetime.timedelta(minutes=5)

    context = {
        'title': assessment_code,
        'assessment': assessment,
        'questions': questions,
        'mcqquestions': mcqquestions,
        'mcqsolutions': mcqsolutions,
        'manager': manager,
        'warnig_time': warning_time,
        'rem_time': rem_time
    }
    if rem_time < 0:
        context['error'] = "Your Time is up"
        return render(request, "assessment/home.html", context)
    return render(request, 'assessment/assessment.html', context)




