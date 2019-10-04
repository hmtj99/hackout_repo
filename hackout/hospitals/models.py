from django.db import models
from django.urls import reverse_lazy


class Hospital(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blood_group = models.CharField(max_length=256)
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="entry")
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.hospital} - {self.blood_group}"

    def get_absolute_url(self):
        return reverse_lazy("hospitals:hospital-detail", kwargs={"pk": self.hospital.pk})
