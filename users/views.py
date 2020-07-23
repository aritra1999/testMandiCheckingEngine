from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

import random
from .email import email_message
from .models import OTPLog, StudentProfile, OrgProfile


def auth_view(request):
    context = {
        "title": "Authentication",
        "reg_error": [],
        "login_error": []
    }

    if request.method == "POST":
        if request.POST.get('form-type') == "login":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect("/staff")
                return redirect("/")
            else:
                context['login_error'].append("Username and password do not match!")

        elif request.POST.get('form-type') == "register":

            if request.POST.get('password1') == request.POST.get('password2'):
                if User.objects.filter(email=request.POST.get('email')).exists():
                    context["reg_error"].append("Email already in use!")
                else:
                    request.session['user_type'] = request.POST.get('user_type')
                    request.session['f_name'] = request.POST.get('f_name')
                    request.session['l_name'] = request.POST.get('l_name')
                    request.session['email'] = request.POST.get('email')
                    request.session['password'] = request.POST.get('password1')

                    otp = random.randint(100000, 999999)

                    message = 'Your OTP is: ' + str(otp)
                    email_message(request.POST.get('email'), 'Registration OTP', message)
                    OTPLog.objects.create(email=request.POST.get('email'), otp=otp).save()
                    print(otp)
                    return redirect("/auth/otp")
            else:
                context["reg_error"].append("Passwords don't match!")

    return render(request, 'users/auth.html', context)


def auth_otp_view(request):
    context = {
        'title': "OTP"
    }
    print(OTPLog.objects.get(email=request.session['email']).otp)
    if request.method == "POST":
        otp = OTPLog.objects.get(email=request.session['email'])
        if int(request.POST.get('otp')) == int(otp.otp):
            User.objects.create_user(
                username=request.session['email'],
                first_name=request.session['f_name'],
                last_name=request.session['l_name'],
                email=request.session['email'],
                password=request.session['password']
            )
            user = authenticate(request, username=request.session['email'], password=request.session['password'])
            if user is not None:
                login(request, user)
            return redirect('/auth/details')
        else:
            context['error'] = "Wrong OTP"
    return render(request, 'users/otp.html', context)


@login_required
def auth_details_view(request):
    context = {
        'title': 'Registration Details'
    }
    if request.session['user_type'] == "organization":
        if request.method == "POST":
            OrgProfile.objects.create(
                user=request.user,
                contact_number=request.POST.get('contact_number'),
                company_name=request.POST.get('company_name'),
                country=request.POST.get('country'),
                website=request.POST.get('website'),
            ).save()
            return redirect('/')
        return render(request, 'users/org.html', context)
    elif request.session['user_type'] == "student":
        if request.method == "POST":
            StudentProfile.objects.create(
                user=request.user,
                contact_number=request.POST.get('contact_number'),
                country=request.POST.get('country'),
                headline=request.POST.get('headline'),
                about_me=request.POST.get('about_me'),
                website=request.POST.get('website'),
                social_website=request.POST.get('social_website'),
                years_exp=request.POST.get('years_exp'),
                jobs_open=request.POST.get('jobs_open'),
            ).save()
            return redirect('/')
        return render(request, 'users/student.html', context)


def test_email_view(request):
    context = {
        'title': 'Test Email Sending'
    }
    if request.method == "POST":
        email = request.POST.get('email')
        message = 'The email function works'

        if email_message(email, 'This is a test email', message):
            context['sent'] = "Message Sent"
        else:
            context['sent'] = "Unknown Error, please try again later"
    return render(request, "users/email_test.html", context)
