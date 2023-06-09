# Generated by Django 4.1.7 on 2023-03-22 16:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tutoria",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("Nombre", models.CharField(max_length=200)),
                ("Tema", models.CharField(max_length=200)),
                ("Estado", models.CharField(max_length=200)),
            ],
        ),
    ]
