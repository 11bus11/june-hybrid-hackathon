# from django.shortcuts import render
# from django.views import generic, View
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect


# def schedule(request):
#     user = request.user
#     context = {
#         'user': user,
#     }
#     return render(request, 'book-appointment.html', context)

# from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
# from django.db.models import Q
from .models import TimeSlot
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TimeSlotForm
from appointments.models import Appointment


class ScheduleListView(LoginRequiredMixin, ListView):
    """
    View for displaying a list of recipes based on search queries and
    categories, or all published recipes if there is no search query.

    Attributes:
        model (Model): The model associated with the view (Timeslot).
        template_name (str): The name of the template used to render the page.
        paginate_by (int): The number of items to paginate by.
    """
    model = TimeSlot
    template_name = 'book-appointment.html'
    login_url = reverse_lazy('index')

    def get_queryset(self):
        # Only return available time slots
        queryset = TimeSlot.objects.filter(is_booked=False)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Adds extra context data, the user object.

        Returns:
            dict: A dictionary containing additional context data.
                - 'user': user object
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
            appointment.save()
            # return redirect('success_page')
        return self.get(request, *args, **kwargs)
