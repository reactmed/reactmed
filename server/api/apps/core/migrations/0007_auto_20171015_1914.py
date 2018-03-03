# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 19:14
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171012_2110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Прием', 'verbose_name_plural': 'Приемы'},
        ),
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'verbose_name': 'Диагноз', 'verbose_name_plural': 'Диагнозы'},
        ),
        migrations.AlterModelOptions(
            name='intind',
            options={'verbose_name': 'Целый показатель', 'verbose_name_plural': 'Целые показатели'},
        ),
        migrations.AlterModelOptions(
            name='medarea',
            options={'verbose_name': 'Медицинская область', 'verbose_name_plural': 'Медицинские области'},
        ),
        migrations.AlterModelOptions(
            name='medication',
            options={'verbose_name': 'Медикаментация', 'verbose_name_plural': 'Медикаментация'},
        ),
        migrations.AlterModelOptions(
            name='medtest',
            options={'verbose_name': 'Тип обследования', 'verbose_name_plural': 'Типы обследования'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Пациент', 'verbose_name_plural': 'Пациенты'},
        ),
        migrations.AlterModelOptions(
            name='realind',
            options={'verbose_name': 'Вещественный показатель', 'verbose_name_plural': 'Вещественные показатели'},
        ),
        migrations.AlterModelOptions(
            name='testrec',
            options={'verbose_name': 'Обследование', 'verbose_name_plural': 'Обследования'},
        ),
        migrations.AlterModelOptions(
            name='textind',
            options={'verbose_name': 'Строковой показатель', 'verbose_name_plural': 'Строковые показатели'},
        ),
        migrations.AlterModelOptions(
            name='treatment',
            options={'verbose_name': 'Лечение', 'verbose_name_plural': 'Лечение'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(verbose_name='Дата приема'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='complaints',
            field=models.TextField(blank=True, null=True, verbose_name='Жалобы пациента'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='core.Patient', verbose_name='Пациент'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Назначено', 'Назначено'), ('Завершено', 'Завершено'), ('Отменено', 'Отменено')], default='Назначено', max_length=30, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='content',
            field=models.BinaryField(verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='test_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TestRec', verbose_name='Обследование'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis',
            field=models.TextField(verbose_name='Диагноз'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis_date',
            field=models.DateField(verbose_name='Дата диагноза'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient', verbose_name='Пациент'),
        ),
        migrations.AlterField(
            model_name='intind',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='intind',
            name='max_critical',
            field=models.IntegerField(blank=True, null=True, verbose_name='Максимальная критическая норма'),
        ),
        migrations.AlterField(
            model_name='intind',
            name='max_norm',
            field=models.IntegerField(blank=True, null=True, verbose_name='Максимальная норма'),
        ),
        migrations.AlterField(
            model_name='intind',
            name='min_critical',
            field=models.IntegerField(blank=True, null=True, verbose_name='Минимальная критическая норма'),
        ),
        migrations.AlterField(
            model_name='intind',
            name='min_norm',
            field=models.IntegerField(blank=True, null=True, verbose_name='Минимальная норма'),
        ),
        migrations.AlterField(
            model_name='intind',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='intind',
            name='short_name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='intind',
            name='unit',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='medarea',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='medarea',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='medarea',
            name='short_name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='drugs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None, verbose_name='Лекарства'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='medication_date',
            field=models.DateField(verbose_name='Дата медикаментации'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient', verbose_name='Пациент'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='summary',
            field=models.CharField(max_length=255, verbose_name='Краткая информация'),
        ),
        migrations.AlterField(
            model_name='medtest',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='medtest',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='medtest',
            name='short_name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес проживания'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], max_length=20, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=20, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='Инвалидность'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Род деятельности'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='omi_card',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='ОМС'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rh_factor',
            field=models.CharField(blank=True, choices=[('Rh+', 'Rh+'), ('Rh-', 'Rh-')], max_length=20, null=True, verbose_name='Резус-фактор'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='surname',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='realind',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='realind',
            name='max_critical',
            field=models.FloatField(blank=True, null=True, verbose_name='Максимальная критическая норма'),
        ),
        migrations.AlterField(
            model_name='realind',
            name='max_norm',
            field=models.FloatField(blank=True, null=True, verbose_name='Максимальная норма'),
        ),
        migrations.AlterField(
            model_name='realind',
            name='min_critical',
            field=models.FloatField(blank=True, null=True, verbose_name='Минимальная критическая норма'),
        ),
        migrations.AlterField(
            model_name='realind',
            name='min_norm',
            field=models.FloatField(blank=True, null=True, verbose_name='Минимальная норма'),
        ),
        migrations.AlterField(
            model_name='realind',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='realind',
            name='short_name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='realind',
            name='unit',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='testrec',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='testrec',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='testrec',
            name='int_inds',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Целые показатели'),
        ),
        migrations.AlterField(
            model_name='testrec',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Тип обследования'),
        ),
        migrations.AlterField(
            model_name='testrec',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_recs', to='core.Patient', verbose_name='Пациент'),
        ),
        migrations.AlterField(
            model_name='testrec',
            name='real_inds',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Вещественные показатели'),
        ),
        migrations.AlterField(
            model_name='testrec',
            name='short_name',
            field=models.CharField(max_length=200, verbose_name='Тип обследования (идентификатор)'),
        ),
        migrations.AlterField(
            model_name='testrec',
            name='summary',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Краткая информация'),
        ),
        migrations.AlterField(
            model_name='testrec',
            name='test_date',
            field=models.DateField(verbose_name='Дата проведения'),
        ),
        migrations.AlterField(
            model_name='testrec',
            name='text_inds',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Строковые показатели'),
        ),
        migrations.AlterField(
            model_name='textind',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='textind',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='textind',
            name='short_name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='textind',
            name='values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None, verbose_name='Принимаемые значения'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='finish_date',
            field=models.DateField(verbose_name='Конец лечения'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient', verbose_name='Пациент'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='start_date',
            field=models.DateField(verbose_name='Начало лечения'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='summary',
            field=models.CharField(max_length=255, verbose_name='Краткая информация'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 15, 19, 14, 18, 871034, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Администратор?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('DOCTOR', 'DOCTOR')], default='DOCTOR', max_length=20, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=30, verbose_name='Фамилия'),
        ),
    ]