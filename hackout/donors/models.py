from django.db import models
from django.contrib.auth.models import User


class Donor(User):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    blood_group = models.CharField(max_length=5)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=300)

    def __str__(self):
        name = f"{self.user.first_name} {self.user.last_name} - {self.blood_group}"
        return name
