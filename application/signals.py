from django.db.models.signals import post_save

from .models import Application
from account.tasks import send_email_to_attorneys, send_email_to_applicant

def create_application(sender, instance, created, **kwargs):
    if created:
        print(instance.get_full_name())
        send_email_to_applicant.delay(email=instance.email, full_name=f"{instance.first_name} {instance.last_name}")
        send_email_to_attorneys.delay(instance.id)


post_save.connect(create_application, sender=Application)