# Generated by Django 5.1.2 on 2024-10-24 00:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event_uci', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comite',
            name='coordinador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comite',
            name='miembros',
            field=models.ManyToManyField(blank=True, related_name='miembros', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipo',
            name='participantes',
            field=models.ManyToManyField(blank=True, related_name='participantes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipo',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_uci.evento'),
        ),
        migrations.AddField(
            model_name='comite',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_uci.evento'),
        ),
        migrations.AddField(
            model_name='evidencia',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_uci.evento'),
        ),
        migrations.AddField(
            model_name='resultado',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_uci.evento'),
        ),
        migrations.AddField(
            model_name='resultado',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_uci.evento'),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
