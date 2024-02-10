from django.db import models

from manufacturer.models import Manufacturer


class Device(models.Model):
    name = models.CharField(max_length=155)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="device")
    price = models.PositiveIntegerField()

    class Meta:
        ordering = ["name"]
