from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import get_object_or_404
from .models import User
from appointments.models import Appointment
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    return render(request, 'users/index.html')
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'index.html', context)


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'patient.html'
    context_object_name = 'user'
    login_url = '/accounts/login/'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = self.get_object()  # Get the user object
        context['appointments'] = Appointment.objects.filter(patient=patient)
        return context
