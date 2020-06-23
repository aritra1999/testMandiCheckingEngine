from .models import Question, Submission, IO

import requests, os, time
import subprocess


def code_checker(request, code, lang, question_hit, username):
    ios = IO.objects.filter(question_hit=question_hit)
    verdict_count = 0
    time_taken = 0.0

    for io in ios:
        test_input = io.input
        test_output = io.output
        run_command = ext = ""
        run_file_name = ("media/Code/" + username + "_" + question_hit)

        if lang == 'c_cpp':
            subprocess.run("g++ " + run_file_name + ".cpp -o " + run_file_name + ".out ", shell=True)
            run_command = ("./" + run_file_name + ".out <" + run_file_name + ".in> " + run_file_name + ".txt")
            ext = ".cpp"
        elif lang == 'python':
            run_command = ("python3 " + run_file_name + ".py <" + run_file_name + ".in> " + run_file_name + ".txt")
            ext = ".py"
        elif lang == 'java':
            run_command = ("java " + run_file_name + ".java <" + run_file_name + ".in> " + run_file_name + ".txt")
            ext = ".java"

        open(run_file_name + ext, "w").write(code)
        open(run_file_name + ".in", "w").write(test_input)

        timeStarted = time.time()
        subprocess.run(run_command, shell=True)
        time_taken += time.time() - timeStarted

        try:
            output = open(run_file_name + ".txt", "r").read()
        except:
            return  0.00, "error"

        if (output).strip() == (test_output).strip():verdict_count += 1
        os.remove(run_file_name + ".txt")

    if verdict_count == len(ios):verdict = True
    else: verdict = False


    return time_taken, verdict


def gen_hit(title):
    hit = ""
    for word in title.split():hit += word[0].upper()
    return hit

