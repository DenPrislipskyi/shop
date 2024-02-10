from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=199)
    country = models.CharField(max_length=155)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
