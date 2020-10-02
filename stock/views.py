from django.shortcuts import render


# Create your views here.
def index(request):    
    return render(request, 'frontend/index.html')
def place(request):    
    return render(request, 'frontend/place.html')
def contact(request):    
    return render(request, 'frontend/contact.html')