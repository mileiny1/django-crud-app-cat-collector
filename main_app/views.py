
from django.http import HttpResponse
from django.shortcuts import render
from .models import Cat
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
# main-app/views.py



class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

    #success_url = '/cats/'
class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']
class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

    #















