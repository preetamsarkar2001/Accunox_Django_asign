

from django.http import HttpResponse
from .rectangle import Rectangle

def rectangle_view(request):
   
    rect = Rectangle(10, 5)
    
   
    dimensions = "\n".join([f"{key}: {value}" for dimension in rect for key, value in dimension.items()])
    return HttpResponse(f"Rectangle Dimensions:\n{dimensions}")
