from django.db import models
from django.forms import ValidationError
from users.models import User
from scheduling.models import TimeSlot


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('patient', 'time_slot')

    def clean(self):
        # Ensure no overlapping bookings for the same patient on the same day
        overlapping_appts = Appointment.objects.filter(
            patient=self.patient,
            time_slotday=self.time_slot.day
        ).exclude(pk=self.pk)  # Exclude self in case of update

        for appointment in overlapping_appts:
            if self.time_slot.overlaps(appointment.time_slot):
                raise ValidationError(
                    'You already have an appointment at this time slot.'
                    )

    def save(self, args, **kwargs):
        self.clean()  # Perform validation
        super().save(args, **kwargs)

    def str(self):
        return f"Booking for {self.patient} on {self.date} at {self.time_slot}"
