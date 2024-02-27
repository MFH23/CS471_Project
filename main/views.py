from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def about(request):
    pass

def contact(request):
    return render(request, 'main/contact.html')

def feedback(request):
    pass

def services(request):
    pass

def appointment(request):
    pass
