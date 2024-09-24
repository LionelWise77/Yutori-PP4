from django.contrib import admin
from .models import Appointment, Service, Client, TreatmentService

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'appointment_date', 'status')  # Added 'client' to display
    list_filter = ('status', 'appointment_date')  # Filter appointments by status and date
    search_fields = ('client__user__username', 'service__name')  # Search by client username and service name

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    search_fields = ['name']  # Search by service name

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')  # Display user, phone, and address
    search_fields = ('user__username', 'phone')  # Search by username and phone number

@admin.register(TreatmentService)
class TreatmentServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Display service name and price
    search_fields = ('name',)  # Search by name