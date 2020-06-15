from .models import Question, Submission, Output, Input

import requests, os, time
import subprocess


def code_checker(request, code, lang, question_hit, username):
    inputs = Input.objects.filter(question_hit=question_hit)
    verdict_count = 0
    verdict = True
    time_taken = 0.0

    for input in inputs:
        test_input = input.input
        test_output = Output.objects.get(question_hit=question_hit, output_number=input.input_number).output
        run_command = ext = ""
        run_file_name = ("media/Code/" + username + "_" + question_hit)

        if lang == 'c_cpp':
            run_command = ("g++ " + run_file_name + ".cpp -o " + run_file_name + ".out && ./" + run_file_name + ".out <" + run_file_name + ".in> " + run_file_name + ".txt")
            ext = ".cpp"
        elif lang == 'python':
            run_command = (
            "python3 " + run_file_name + ".py <" + run_file_name + ".in> " + run_file_name + ".txt")
            ext = ".py"

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

    if verdict_count == len(inputs):verdict = True
    else: verdict = False


    return time_taken, verdict

