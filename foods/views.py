from typing import List
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Food, Comment
from .forms import CommentForm
# Create your views here.


class FoodListView(ListView):
    model = Food
    template_name = "foods/index.html"
    context_object_name = "foods"


# class FoodDetailView(DetailView):
    # model = Food
    # template_name = "foods/food_details.html"
    # context_object_name = "foods"
    

def food_view(request, id):

    food = Food.get_object_or_404(id=id)
    comment = Comment.objects.all()

    new_comment = CommentForm()
    
    if request.method == 'POST':
        new_comment = CommentForm(request.POST)
        if new_comment.is_valid():
            new_comment.save()
    else:
        new_comment = CommentForm()

    context={
        "comments":comment,
        "foods":food,
        "form":new_comment,
    }
    return render(request, 'foods/food_details.html', context)

class FoodMenuListView(ListView):
    model = Food
    context_object_name = 'foods'
    template_name='foods/menu.html'


class AboutListView(ListView):
    model = Food
    context_object_name = 'foods'
    template_name = 'foods/about.html'

class GalleryView(ListView):
    model = Food
    template_name = 'foods/gallery.html'

class StuffView(ListView):
    model = Food
    context_object_name = 'foods'
    template_name = 'foods/stuff.html'

class ComingSoonView(ListView):
    model = Food
    template_name = 'foods/coming soon.html'


