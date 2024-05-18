from django.shortcuts import render ,HttpResponse,redirect,get_object_or_404 # the last import it is an error handling if the object is not found
from .models import Contact , Appointment, Doctor, Patient
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm,AppointmentForm
from django.contrib.auth.decorators import login_required


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


def services(request):
    pass




# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return render(request, 'main/home.html')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return render(request, 'main/home.html')


############################################################################## 
'''
@login_required
def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = Patient.objects.get(user=request.user)
            appointment.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    
    return render(request, 'main/make_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'main/appointment_success.html')'''

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = Patient.objects.get(user=request.user)
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'main/appointment_create.html', {'form': form})

@login_required
def update_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'main/appointment_update.html', {'form': form, 'appointment': appointment})

@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'main/appointment_detail.html', {'appointment': appointment})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(patient__user=request.user)
    return render(request, 'main/appointment_list.html', {'appointments': appointments})

@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'main/appointment_confirm_delete.html', {'appointment': appointment})