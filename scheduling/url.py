from django.urls import path

from . import views

app_name = "scheduling"

urlpatterns = [
    path("", views.day_of_week, name ="day_of_week")
]

