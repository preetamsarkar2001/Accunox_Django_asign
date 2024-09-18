from django.shortcuts import render

# Create your views here.
# question2/views.py
from django.http import HttpResponse
from .signals import signal_for_thread_test
import threading

def trigger_signal_for_thread_test(request):
    print(f"View thread: {threading.current_thread().name}")
    signal_for_thread_test.send(sender=None)
    return HttpResponse("Signal triggered, check terminal for thread information.")
