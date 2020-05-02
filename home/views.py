from django.shortcuts import render

# Create your views here.

def home(request):
    """A view that displays the index page"""
    return render(request, "home.html")

def about(request):
    """A view that displays the index page"""
    return render(request, "about.html")

def contact(request):
    """A view that displays the index page"""
    return render(request, "contact.html")

def spare(request):
    """A view that displays the index page"""
    return render(request, "spare.html")
