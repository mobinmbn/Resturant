from django.shortcuts import render
from django.views.generic import CreateView
from .models import Reservation
from .forms import ReservationForm

# Create your views here.

def reserv_view(request):
    reserv_form = ReservationForm()
    
    if request.method == 'POST':
        reserv_form = ReservationForm(request.POST)
        if reserv_form.is_valid():
            reserv_form.save()
    else:
        reserv_form = ReservationForm()

    context = {
        "form":reserv_form,
    }

    return render(request, 'reserve/reservation.html', context)
