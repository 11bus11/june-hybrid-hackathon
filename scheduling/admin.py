from django.contrib import admin
from .models import Day, TimeSlot

# Register your models here.
class TimeSlotAmin(admin.ModelAdmin):
    list_display = ("start_time", "end_time", "day")


admin.site.register(Day)
admin.site.register(TimeSlot)
