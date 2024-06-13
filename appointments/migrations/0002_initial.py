# Generated by Django 4.2.13 on 2024-06-13 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scheduling', '0001_initial'),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.timeslot'),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('patient', 'time_slot')},
        ),
    ]
