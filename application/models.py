from django.db import models
from django.utils.translation import gettext_lazy as _

class Application(models.Model):
    class ApplicationStatus(models.TextChoices):
        PENDING = "pending", _('Pending')
        REACHED_OUT = "reached_out", _('Reached Out')

    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    email = models.EmailField(_('email'), max_length=125)
    resume = models.FileField(_('resume/cv'), upload_to="resumes/")
    status = models.CharField(_('status'), max_length=60, choices=ApplicationStatus.choices,
                              default=ApplicationStatus.PENDING)

    class Meta:
        verbose_name = _('application')
        verbose_name_plural = _('applications')

    def __str__(self):
        return f"ID: {self.pk} | Email: {self.email} | Status: {self.status}"


    def get_full_name(self):
        return f"{self.first_name}-{self.last_name}"