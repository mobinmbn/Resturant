from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact
from .forms import ContactForm

# Create your views here.

# class ContactView(ListView):
#     model = Contact
#     template_name = 'contact/contact.html'

def contact_form(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
    else:
        contact_form = ContactForm()

    context = {
        "form":contact_form,
    }

    return render(request, 'contact/contact.html', context)
