from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'booking_date', 'number_of_guests']