from django.db import models


# Create your models here.
class Day(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date.strftime('%a, %B %d, %Y')


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.ForeignKey(
        Day, related_name='time_slots', on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)

    def overlaps(self, other):
        return (
            self.start_time < other.end_time and
            self.end_time > other.start_time
        )

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} - {
            self.end_time.strftime('%H:%M')} on {self.day}"
