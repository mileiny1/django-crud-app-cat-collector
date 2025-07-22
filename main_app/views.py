from django.shortcuts import render
from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
# Create about view function
def about(request):
    return render(request, 'about.html')


