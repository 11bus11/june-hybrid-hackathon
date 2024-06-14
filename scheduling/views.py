
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView
# from django.db.models import Q
from .models import TimeSlot
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TimeSlotForm
from appointments.models import Appointment


class ScheduleListView(LoginRequiredMixin, ListView):
    """
    View for displaying a list of available timeslots.

    Attributes:
        model (Model): The model associated with the view (Timeslot).
        template_name (str): The name of the template used to render the page.
    """
    model = TimeSlot
    template_name = 'book-appointment.html'
    login_url = '/accounts/login/'

    def get_queryset(self):
        # Only return available time slots
        queryset = TimeSlot.objects.filter(is_booked=False)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Adds extra context data.

        Returns:
            dict: A dictionary containing additional context data.
                - 'user': user object
                - 'form': the form to book an appointment
        """
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['form'] = TimeSlotForm()

        return context

    def post(self, request, *args, **kwargs):
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            timeslot = form.cleaned_data['timeslot']
            timeslot.is_booked = True
            timeslot.save()

            appointment = Appointment(
                patient=request.user,
                time_slot=timeslot,
                appointment_reason=form.cleaned_data['reason']
            )
            appointment.save(args)
            # return redirect('success_page')
        return self.get(request, *args, **kwargs)
