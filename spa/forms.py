"""This module contains forms for managing appointments and user profiles."""

from django import forms
from .models import Appointment, Service, Profile
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AppointmentForm(forms.ModelForm):
    """Form for creating and updating appointments."""

    class Meta:
        """Meta class for AppointmentForm."""
        model = Appointment
        fields = ['service', 'appointment_date']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local', 
                'class': 'form-control',
                'format': '%Y-%m-%dT%H:%M'  # Format for 'datetime-local'
            }),
        }

    def clean_appointment_date(self):
        """Validate that the appointment date is not in the past."""
        appointment_date = self.cleaned_data.get('appointment_date')
        if appointment_date < timezone.now():
            raise ValidationError("The appointment date cannot be in the past.")
        return appointment_date

    def __init__(self, *args, **kwargs):
        """Initialize the form and set the queryset for services."""
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.all()


class UserUpdateForm(forms.ModelForm):
    """Form for updating user information."""

    class Meta:
        """Meta class for UserUpdateForm."""
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """Form for updating user profile information."""

    class Meta:
        """Meta class for ProfileUpdateForm."""
        model = Profile
        fields = ['address', 'phone']

class RegisterForm(UserCreationForm):
    """Form for registering a new user with email."""
    email = forms.EmailField()

    class Meta:
        """Meta class for RegisterForm."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']    
