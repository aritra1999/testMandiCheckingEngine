import requests
import os

from django.conf import settings
from django.shortcuts import render
from .models import Question, Submission, Output, Input
import subprocess

def code_checker(request, code, lang, question_hit, username):
    inputs = Input.objects.filter(question_hit=question_hit)
    verdict_count = 0
    time_taken = 0.0
    verdict = True

    for input in inputs:
        test_input = input.input
        test_output = Output.objects.get(question_hit=question_hit, output_number=input.input_number).output
        run_file_name = run_command = ext = ""

        if lang == 'C++':
            run_file_name = ("media/Code/" + username + "_" + question_hit)
            run_command = ("g++ " + run_file_name + ".cpp -o " + run_file_name + ".out && ./" + run_file_name + ".out <" + run_file_name + ".in> " + run_file_name + ".txt")
            ext = ".cpp"

        open(run_file_name + ext, "w").write(code)
        open(run_file_name + ".in", "w").write(test_input)

        subprocess.run(run_command, shell=True)
        output = open(run_file_name + ".txt", "r").read()

        if (output).strip() == (test_output).strip():verdict_count += 1


    if verdict_count == len(inputs):verdict = True
    else: verdict = False

    return time_taken, verdict


def dashboard_view(request):
    questions = Question.objects.all()
    context = {
        "title": "Dashboard",
        "questions": questions
    }

    return render(request, 'dashboard/home.html', context)


def question_details_view(request, hit):
    question = Question.objects.get(hit=hit)
    context = {
        "title": hit,
        "question": question
    }

    if request.method == "POST":
        user = "test-user"
        question_hit = hit
        solution = request.POST.get('solution')
        language = request.POST.get('language')
        time_taken, verdict = code_checker(request, solution, language, question_hit, username="test_user")

        if verdict == True:context["result"] = "Correct Answer"
        else: context["result"] = "Wrong Answer"

        Submission.objects.create(user=user, question_hit=question_hit, time_taken=time_taken, verdict=verdict, solution=solution, language=language).save()

    return render(request, 'dashboard/question.html', context)