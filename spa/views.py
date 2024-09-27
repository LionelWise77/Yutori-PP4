from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, TreatmentService, Appointment, Invoice, Service
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.

@login_required
def service_list(request):
    services = TreatmentService.objects.all()
    return render(request, 'spa/service_list.html', {'services': services})

@login_required
def book_appointment(request):
    try:
        # Ensure that the user has a client
        client = request.user.client
    except Client.DoesNotExist:
        # Create a client object for the user if it doesn't exist
        client = Client.objects.create(user=request.user)
        
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user.client
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'spa/book_appointment.html', {'form': form})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(client=request.user.client)
    return render(request, 'spa/appointment_list.html', {'appointments': appointments})

@login_required
def view_invoice(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    # Ensuring the appointment belongs to the client
    if appointment.client != request.user.client:
        return redirect('appointment_list')  # Redirecting if the user does not own the appointment
    
    invoice = get_object_or_404(Invoice, appointment=appointment)
    return render(request, 'spa/invoice_detail.html', {'invoice': invoice})


def index(request):
    
    return render(request, 'index.html',)    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirigir al cliente a una página después del registro
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(client=request.user.client)

    if request.method == 'POST':
        # Eliminar cita
        if 'delete' in request.POST:
            appointment_id = request.POST.get('appointment_id')
            appointment = get_object_or_404(Appointment, id=appointment_id)
            if appointment.client == request.user.client:
                appointment.delete()
                return redirect('appointment_list')
        # Reprogramar cita
        elif 'reschedule' in request.POST:
            appointment_id = request.POST.get('appointment_id')
            appointment = get_object_or_404(Appointment, id=appointment_id)
            if appointment.client == request.user.client:
                form = AppointmentForm(request.POST, instance=appointment)
                if form.is_valid():
                    form.save()
                    return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'spa/appointment_list.html', {'appointments': appointments, 'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # redirigir a la página principal u otra tras el login
    else:
        form = AuthenticationForm()
    return render(request, 'spa/login.html', {'form': form})