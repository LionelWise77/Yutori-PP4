"""This module contains the views for the spa application."""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Appointment, Service, Profile
from .forms import AppointmentForm, UserUpdateForm, ProfileUpdateForm, RegisterForm
from datetime import datetime, date
from django.utils import timezone
from django.utils.timezone import localtime, now




def index(request):
    """Render the homepage with information about whether the user is an admin or a customer."""
    is_admin = request.user.groups.filter(name='Admin').exists() if request.user.is_authenticated else False
    is_customer = request.user.groups.filter(name='Customer').exists() if request.user.is_authenticated else False
    return render(request, 'spa/index.html', {'is_admin': is_admin, 'is_customer': is_customer})

def service_list(request):
    """Display a list of all services."""
    services = Service.objects.all()
    is_admin = request.user.groups.filter(name='Admin').exists()
    is_customer = request.user.groups.filter(name='Customer').exists()
    return render(request, 'spa/service_list.html', {'services': services, 'is_admin': is_admin, 'is_customer': is_customer})



@login_required
def book_appointment(request, service_id=None):
    is_admin = request.user.groups.filter(name="Admin").exists()
    service = get_object_or_404(Service, id=service_id) if service_id else None
    
    min_datetime = localtime(now()).strftime("%Y-%m-%dT%H:%M")
    

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        datetime_str = request.POST.get("datetime")  # Nuevo campo combinado

        if form.is_valid() and datetime_str:
            try:
                combined_dt = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M")
                combined_dt = timezone.make_aware(combined_dt)
                
                if combined_dt < timezone.now():
                    messages.error(request, "You cannot select a past date and time.")
                else:
                    appointment = form.save(commit=False)
                    appointment.client = request.user.client
                    appointment.appointment_date = combined_dt
                    appointment.save()
                    messages.success(request, "Appointment booked successfully.")
                    return redirect("appointment_list")
            except ValueError:
                messages.error(request, "Invalid datetime format.")
        else:
            messages.error(request, "Please provide a valid date and time.")
    else:
        form = AppointmentForm(initial={'service': service})

    return render(request, 'spa/book_appointment.html', {'form': form, 'is_admin': is_admin, 'min_datetime': min_datetime})



@login_required
def appointment_list(request):
    """Display a list of appointments for the logged-in client."""
    appointments = Appointment.objects.filter(client=request.user.client)
    return render(request, 'spa/appointment_list.html', {'appointments': appointments})

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print("✔️ Ambos formularios son válidos")
            try:
                user = user_form.save(commit=False)
                raw_password = user_form.cleaned_data['password']
                user.set_password(raw_password)
                user.save()

                customer_group = Group.objects.get(name='Customer')
                user.groups.add(customer_group)

                profile = user.profile
                profile.phone = profile_form.cleaned_data.get('phone')
                profile.address = profile_form.cleaned_data.get('address')
                profile.save()

                login(request, user)
                print("✔️ Usuario autenticado:", request.user.is_authenticated)
                print("🔐 Sesión ID:", request.session.session_key)
                return redirect('home')
            except Exception as e:
                print("❌ Error durante el guardado:", e)
                user_form.add_error(None, f"Ocurrió un error: {e}")
        else:
            print("❌ Formularios inválidos")
            print("Errores user_form:", user_form.errors)
            print("Errores profile_form:", profile_form.errors)

    else:
        user_form = RegisterForm()
        profile_form = ProfileUpdateForm()

    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def my_appointments(request):
    """Display and manage appointments for the logged-in client."""
    appointments = Appointment.objects.filter(client=request.user.client)

    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        appointment = get_object_or_404(Appointment, id=appointment_id)

        if 'delete' in request.POST:
            if appointment.client == request.user.client:
                appointment.delete()
                messages.success(request, 'Appointment deleted successfully.')
                return redirect('my_appointments')

        elif 'reschedule' in request.POST:
            if appointment.client == request.user.client:
                new_datetime_str = request.POST.get('new_datetime')

            if new_datetime_str:
              try:
                # Convertir el string en objeto datetime
                    new_datetime_obj = datetime.strptime(new_datetime_str, '%Y-%m-%dT%H:%M')

                # Validar que la nueva fecha no esté en el pasado
                    if new_datetime_obj < datetime.now():
                        messages.error(request, 'You cannot select a past date and time.')
                    else:
                        appointment.appointment_date = new_datetime_obj
                        appointment.save()
                        messages.success(request, 'Appointment rescheduled successfully.')
              except ValueError:
                    messages.error(request, 'Invalid date and time format.')
        else:
            messages.error(request, 'Please provide a valid date and time.')


    return render(request, 'spa/appointment_list.html', {'appointments': appointments})

def login_view(request):
    """Handle user login."""
    if request.method == 'POST':    
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'spa/login.html', {'form': form})

def logout_view(request):
    """Handle user logout and redirect to the home page."""
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('home')

@login_required
def profile_view(request):
    """Display and allow the user to update their profile information."""
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'spa/profile.html', context)

def admin_required(user):
    """Check if the user belongs to the 'Admin' group."""
    return user.groups.filter(name='Admin').exists()

@user_passes_test(admin_required)
def admin_view(request):
    """Display the admin dashboard."""
    return render(request, 'spa/admin_dashboard.html')

def some_view(request):
    """Render a template with admin information."""
    context = {
        'is_admin': request.user.groups.filter(name='Admin').exists(),
    }
    return render(request, 'spa/your_template.html', context)