# Generated by Django 4.1.7 on 2023-03-22 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tutorias", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="tutoria",
            name="tutor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tutor_tutorias",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="tutoria",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usuario_tutorias",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
