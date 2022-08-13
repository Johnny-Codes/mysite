from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/base.html')

def css_playground(request):
    return render(request, "home/cssplayground.html")

def js_playground(request):
    return render(request, "home/jsplayground.html")

def django_projects(request):
    return render(request, "home/djangoprojects.html")