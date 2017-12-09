# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 20:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_date', models.DateTimeField()),
                ('info', models.TextField()),
                ('complaints', models.TextField()),
                ('status', models.CharField(choices=[('Назначено', 'Назначено'), ('Завершено', 'Завершено'), ('Отменено', 'Отменено')], default='Назначено', max_length=30)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='core.Patient')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
                'db_table': 'appointment',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 9, 20, 41, 15, 646911, tzinfo=utc)),
        ),
    ]