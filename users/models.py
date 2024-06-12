from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    social_security_no = models.CharField(max_length=20, unique=True)
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    post_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def str(self):
        return f"{self.first_name} {self.last_name}, {self.social_security_no}"
