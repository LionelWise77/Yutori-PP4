from django.contrib import admin
from .models import Appointment, Service, Client, Profile

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'appointment_date', 'status')  
    list_filter = ('status', 'appointment_date')  
    search_fields = ('client__user__username', 'service__name')  

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    search_fields = ['name']  # Search by service name

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')  
    search_fields = ('user__username', 'phone')  

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone']
