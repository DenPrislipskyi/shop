# Generated by Django 5.0.2 on 2024-02-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("device", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "devices",
                    models.ManyToManyField(related_name="carts", to="device.device"),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
    ]