from django.shortcuts import render ,HttpResponse
from .models import Contact


# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def about(request):
    pass

def contact(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        
        # basic validation
        if first_name and last_name and email and message:
            contact = Contact(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                message=message
            )
            contact.save()
            return HttpResponse("<h1>Thanks</h1>")
        else:
            return HttpResponse("<h1>Error: Please fill in all required fields</h1>")


    return render(request, 'main/contact.html')

def feedback(request):
    pass

def services(request):
    pass

def appointment(request):
    pass
