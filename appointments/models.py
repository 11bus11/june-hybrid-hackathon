from django.db import models
from django.forms import ValidationError
from users.models import User
from scheduling.models import TimeSlot


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    appointment_reason = models.CharField(max_length=50, default="")

    class Meta:
        unique_together = ('patient', 'time_slot')

    def clean(self):
        # Ensure no overlapping bookings for the same patient on the same day
        overlapping_appts = Appointment.objects.filter(
            patient=self.patient,
            time_slot__day=self.time_slot.day
        ).exclude(pk=self.pk)  # Exclude self in case of update

        for appointment in overlapping_appts:
            if self.time_slot.overlaps(appointment.time_slot):
                raise ValidationError(
                    'You already have an appointment at this time slot.'
                    )

    def save(self, *args, **kwargs):
        self.clean()  # Perform validation
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking for {self.patient} on {self.time_slot}"
