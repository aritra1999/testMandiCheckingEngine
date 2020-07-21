from .models import Question, Submission

import requests, os, time
import subprocess


def code_checker(request, code, lang, question_hit, username):
    ios = IO.objects.filter(question_hit=question_hit)
    verdict_count = 0
    time_taken = 0.0

    code_file_path = ("media/Code/" + username + "_" + question_hit)
    for number in range(1, 11):
        run_command = ""
        ext = ""

        input_file = "media/IO/" + str(question_hit) + "/input" + str(number) + ".in"
        output_file = "media/IO/" + str(question_hit) + "/output" + str(number) + ".out"

        test_output = open(output_file).read()

        if lang == 'c_cpp':
            subprocess.run("gcc " + code_file_path + ".c -o " + code_file_path, shell=True)
            run_command = ("./" + code_file_path + " <" + input_file + "> " + code_file_path + ".out")
            ext = ".c"
        elif lang == 'c_plus':
            subprocess.run("g++ " + code_file_path + ".cpp -o " + code_file_path, shell=True)
            run_command = ("./" + code_file_path + " <" + input_file + "> " + code_file_path + ".out")
            ext = ".cpp"
        elif lang == 'python3':
            run_command = ("python3 " + code_file_path + ".py <" + input_file + "> " + code_file_path + ".out")
            ext = ".py"

        elif lang == 'python2':
            run_command = ("python2 " + code_file_path + ".py <" + input_file + "> " + code_file_path + ".out")
            ext = ".py"
        elif lang == 'javascript':
            run_command = ("node " + code_file_path + ".js <" + input_file + "> " + code_file_path + ".out")
            ext = ".js"
        elif lang == 'java':
            run_command = ("java " + code_file_path + ".java <" + input_file + "> " + code_file_path + ".out")
            ext = ".java"
        elif lang == 'r':
            run_command = ("Rscript " + code_file_path + ".R <" + input_file + "> " + code_file_path + ".out")
            ext = ".R"

        print("Command: ", run_command)
        open(code_file_path + ext, "w").write(code)

        timeStarted = time.time()
        process = subprocess.run(run_command, shell=True)
        time_taken += time.time() - timeStarted

        try:
            output = open(code_file_path + ".out", "r").read()
        except:
            return 0.00, "error"

        if (output).strip() == (test_output).strip():
            verdict_count += 1
        # os.remove(code_file_path + ".out")

    print("Count: ", verdict_count)
    if verdict_count == 10:
        verdict = True
    else:
        verdict = False

    return (time_taken/10), verdict


def gen_hit(title):
    hit = ""
    for word in title.split(): hit += word[0].upper()
    return hit
