from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, TreatmentService, Appointment, Invoice
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def service_list(request):
    services = TreatmentService.objects.all()
    return render(request, 'spa/service_list.html', {'services': services})

@login_required
def book_appointment(request):
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
    invoice = Invoice.objects.get(appointment=appointment)
    return render(request, 'spa/invoice_detail.html', {'invoice': invoice})


def appointment_list(request):
    user = request.user
    try:
        client = user.client  # This line raises the error if the user has no client
        appointments = client.appointments.all()
    except Client.DoesNotExist:
        # Handle the case where the user does not have a client
        appointments = []
    
    context = {
        'appointments': appointments
    }
    return render(request, 'spa/appointments_list.html', context)