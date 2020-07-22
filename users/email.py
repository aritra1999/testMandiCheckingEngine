from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


def email_message(email_to, subject, body):
    email_from = settings.EMAIL_HOST_USER
    try:
        send_mail(subject, body, email_from, [email_to], fail_silently=False)
        return True
    except:
        return False


