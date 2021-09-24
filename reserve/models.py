from django.db import models
from django.db.models.enums import IntegerChoices
from django.utils.translation import gettext as _

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    phone = models.CharField(_("Phone Number"), max_length=15)
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("Time"), auto_now=False, auto_now_add=False)
    person = models.PositiveIntegerField(_("Person"), default=1)

    def __str__(self):
        return f'{self.name} / {self.date}'
