
from django.http import HttpResponse
from django.shortcuts import render
from .models import Cat
# Home view


def home(request):
    return render(request, 'home.html')

# About view
def about(request):
    return render(request, 'about.html')



# Cat index view
def cat_index(request):
   cats = Cat.objects.all()  # look familiar?
   return render(request, 'cats/index.html', {'cats': cats})

# Cat detail view
def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)  # get the cat by id
    return render(request, 'cats/detail.html', {'cat': cat})




