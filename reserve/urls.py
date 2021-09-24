from django.urls.conf import path

from . import views

urlpatterns = [
    path('', views.reserv_view ,name="reservation"),
]
