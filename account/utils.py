from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.contrib.auth import get_user_model

from application.models import Application
from .templates import EMAIL_MESSAGE_TO_PROSPECT_TEMPLATE, EMAIL_MESSAGE_TO_ATTORNEY_TEMPLATE

User = get_user_model()

def send_email_for_applicant(email, full_name):
    message = EMAIL_MESSAGE_TO_PROSPECT_TEMPLATE.format(name=full_name)
    send_mail(
        subject="Thank you for your submitting",
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )


def send_email_for_attorneys(application: Application):
    attorney_emails = User.objects.filter(role=User.UserRole.ATTORNEY).values_list('email', flat=True)
    message = EMAIL_MESSAGE_TO_ATTORNEY_TEMPLATE.format(
        first_name=application.first_name,
        last_name=application.last_name,
        email=application.email,
        file_link=settings.MEDIA_URL + application.resume.url
    )
    send_mail(
        subject="New application has submitted",
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=attorney_emails,
    )
