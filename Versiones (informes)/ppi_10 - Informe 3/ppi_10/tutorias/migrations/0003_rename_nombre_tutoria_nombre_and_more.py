# Generated by Django 4.1.7 on 2023-03-27 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorias', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutoria',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='tutoria',
            old_name='Tema',
            new_name='tema',
        ),
        migrations.RemoveField(
            model_name='tutoria',
            name='Estado',
        ),
        migrations.AddField(
            model_name='tutoria',
            name='lugar',
            field=models.CharField(default='Biblioteca', max_length=200),
        ),
        migrations.AddField(
            model_name='tutoria',
            name='estado',
            field=models.CharField(default='Solicitada', max_length=200),
        ),
    ]