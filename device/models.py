import uuid

from django.db import models

from manufacturer.models import Manufacturer


class Device(models.Model):
    name = models.CharField(max_length=155)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="device")
    price = models.PositiveIntegerField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="device")
    tag = models.ManyToManyField("Tag", related_name="device")
    image = models.ImageField(upload_to="upload_models", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            ext = self.image.name.split(".")[-1]
            self.image.name = f"{uuid.uuid4()}.{ext}"
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
