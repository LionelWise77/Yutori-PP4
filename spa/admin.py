"""This file registers models in the Django admin site."""

from django.contrib import admin
from .models import Appointment, Service, Client, Profile

# Register your models here.


# Create the appointment list in the admin
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Admin view for managing appointments."""

    list_display = ('client', 'service', 'appointment_date', 'status')
    list_filter = ('status', 'appointment_date')
    search_fields = ('client__user__username', 'service__name')


# Create the services admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin view for managing services."""

    list_display = ['name', 'description', 'price']
    search_fields = ['name']


# Create a client admin
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Admin view for managing clients."""

    list_display = ('user', 'phone', 'address')
    search_fields = ('user__username', 'phone')


# Create a profile admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin view for managing user profiles."""

    list_display = ['user', 'address', 'phone']
