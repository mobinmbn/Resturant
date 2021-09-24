from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"))
    person = models.PositiveIntegerField(_("Person"))
    message = models.TextField(_("Message"))
    add_time = models.DateTimeField(_("Date & Time"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


