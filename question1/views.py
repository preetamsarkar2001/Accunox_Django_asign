from django.shortcuts import render

# Create your views here.
# signals_test/views.py
from django.http import HttpResponse
from .signals import my_signal

def home(request):
    return render(request,"index.html")

def trigger_signal_view(request):
    print("Before triggering the signal.")
    my_signal.send(sender=None)
    print("After triggering the signal.")
    return HttpResponse("Signal triggered.")
