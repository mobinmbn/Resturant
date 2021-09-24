from django.urls.conf import path
from . import views

urlpatterns = [
    path("home/", views.FoodListView.as_view(), name="home"),
    path("menu/", views.FoodMenuListView.as_view(), name="menu"), 
    path("about/", views.AboutListView.as_view(), name="about"), 
    path("gallery/", views.GalleryView.as_view(), name="gallery"), 
    path("stuff/", views.StuffView.as_view(), name="stuff"), 
    path("coming-soon/", views.ComingSoonView.as_view(), name="coming_soon"), 
    path("food/<int:id>/", views.food_view, name="foods_detail"),
]
