from django.db.models.base import Model
from django.forms import ModelForm
from .models import Reservation

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'