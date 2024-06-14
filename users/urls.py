from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientDetailView.as_view(), name='patient'),
]
