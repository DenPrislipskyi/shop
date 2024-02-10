# Generated by Django 5.0.2 on 2024-02-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Manufacturer",
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
                ("name", models.CharField(max_length=199)),
                ("country", models.CharField(max_length=155)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]