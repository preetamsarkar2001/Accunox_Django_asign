from django.shortcuts import render


from django.http import HttpResponse
from .models import TestModel

def test_signal_transaction_view(request):
    
    TestModel.objects.create(name="Test")
    return HttpResponse("Signal triggered, check terminal for transaction information.")
