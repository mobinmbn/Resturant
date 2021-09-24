from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
# Create your models here.


class Food(models.Model):
    CATEGORY =(
        (0, 'Select item'),
        (1, 'Drink'),
        (2, 'Lunch'),
        (3, 'Dinner'),
    )

    name = models.CharField(_("Name"), max_length=50, null=False)
    summeryDes = models.CharField(_("Summery Description"), max_length=250, default="") 
    description = models.TextField(_("Description"), null=False)
    rate = models.IntegerField(_("Rate"), default=0)
    price = models.PositiveIntegerField(_("Price"), null=False)
    photo = models.ImageField(_("Photo"), upload_to="foodsPic", height_field=None, width_field=None, max_length=None, null=False)
    time = models.PositiveIntegerField(_("Bake time"))
    add_time = models.DateTimeField(_("Add time"), auto_now=False, auto_now_add=True)
    category = models.IntegerField(_("Category"), choices=CATEGORY, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('foods_detail', kwargs={'id': self.pk})

class Comment(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    message = models.TextField(_("Message"))
    add_time = models.DateTimeField(_("Date and Time"), auto_now=False, auto_now_add=True)
    comment = models.ForeignKey("Food", verbose_name=_("Comment"), on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('foods_detail', kwargs={'id': self.pk})