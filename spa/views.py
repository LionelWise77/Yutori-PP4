from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Appointment, Service
from .forms import AppointmentForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.

@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'spa/service_list.html', {'services': services})

@login_required
def book_appointment(request, service_id=None):
    if service_id:
        service = get_object_or_404(Service, id=service_id)
    else:
        service = None

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user.client
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(initial={'service': service})

    return render(request, 'spa/book_appointment.html', {'form': form})


@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(client=request.user.client)
    return render(request, 'spa/appointment_list.html', {'appointments': appointments})

def index(request):
    
    return render(request, 'index.html',)    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(client=request.user.client)

    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        appointment = get_object_or_404(Appointment, id=appointment_id)

        # Handle appointment deletion
        if 'delete' in request.POST:
            if appointment.client == request.user.client:
                appointment.delete()
                messages.success(request, 'Appointment deleted successfully.')
                return redirect('my_appointments')

        # Handle appointment rescheduling
        elif 'reschedule' in request.POST:
            if appointment.client == request.user.client:
                new_date = request.POST.get('new_date')  # Obtener la nueva fecha del formulario
                if new_date:  # Verificar que se haya enviado una nueva fecha
                    try:
                        # Convertir la fecha a DateTimeField y actualizar la cita
                        appointment.appointment_date = new_date
                        appointment.save()
                        messages.success(request, 'Appointment rescheduled successfully.')
                    except ValueError:
                        messages.error(request, 'Invalid date format.')
                else:
                    messages.error(request, 'Please provide a valid date for rescheduling.')
                return redirect('my_appointments')

    return render(request, 'spa/appointment_list.html', {'appointments': appointments})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  
    else:
        form = AuthenticationForm()
    return render(request, 'spa/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def profile(request):
    return render(request, 'spa/profile.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'spa/profile.html', context)    