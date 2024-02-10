from django.db import models

from device.models import Device
from shop_config import settings


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    devices = models.ManyToManyField(Device, related_name="carts")

    class Meta:
        ordering = ["-id"]

    # def __str__(self):
    #     return self.user
