from celery import shared_task

from application.models import Application
from .utils import send_email_for_applicant, send_email_for_attorneys

@shared_task(name="send_email_to_applicant")
def send_email_to_applicant(email, full_name):
    send_email_for_applicant(email, full_name)

@shared_task(name="send_email_to_attorneys")
def send_email_to_attorneys(application_id):
    application = Application.objects.get(id=application_id)
    send_email_for_attorneys(application=application)