from django import forms
from .models import TimeSlot


class TimeSlotForm(forms.Form):
    print("Inside form")
    timeslot = forms.ModelChoiceField(
        queryset=TimeSlot.objects.filter(is_booked=False),
        widget=forms.RadioSelect
    )
    reason = forms.CharField(
        max_length=50,
        label='Reason for appointment',
        widget=forms.TextInput(attrs={'placeholder': 'Enter reason for appointment'})
    )
