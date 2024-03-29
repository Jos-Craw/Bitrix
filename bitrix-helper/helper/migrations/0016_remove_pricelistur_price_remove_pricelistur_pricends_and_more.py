# Generated by Django 4.2.6 on 2024-03-26 06:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0015_applicationf_is_active_applicationu_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricelistur',
            name='price',
        ),
        migrations.RemoveField(
            model_name='pricelistur',
            name='priceNDS',
        ),
        migrations.AddField(
            model_name='pricelistur',
            name='priceNDS_first',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Тариф с НДС - единичное'),
        ),
        migrations.AddField(
            model_name='pricelistur',
            name='priceNDS_next',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Тариф с НДС - последующее'),
        ),
        migrations.AddField(
            model_name='pricelistur',
            name='price_first',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Тариф без НДС - единичное'),
        ),
        migrations.AddField(
            model_name='pricelistur',
            name='price_next',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Тариф без НДС - последующее'),
        ),
    ]
