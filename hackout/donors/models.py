from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Donor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    blood_group = models.CharField(max_length=5)
    phone = models.BigIntegerField()
    city = models.CharField(max_length=300)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def __str__(self):
        name = f"{self.user.first_name} {self.user.last_name} - {self.blood_group}"
        return name

    def get_absolute_url(self):
        return reverse("donor-detail", kwargs={"pk": self.pk})
