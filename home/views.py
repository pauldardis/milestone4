from django.shortcuts import render,redirect, reverse
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import os

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


def contact_success(request):
    """A view that displays the index page"""
    return render(request, "contact_success.html")

def spare(request):
    """A view that displays the index page"""
    return render(request, "spare.html")



def send_email(request):
    name = request.POST.get('user_name')
    subject = request.POST.get('subject')
    message = request.POST.get('text')
    from_email = request.POST.get('user_email')
    the_message = "From: " + name + " Email: " + from_email + " Message: " + message
    if subject and message and from_email:
        try:
            send_mail(subject, the_message, from_email, [os.environ.get('EMAIL')])
            return HttpResponse('Invalid header found.')
        return render(request, 'contact_success.html')
    else:
        messages.error(request, "Please fill out all fields")
      
        return redirect(reverse('contact'))
