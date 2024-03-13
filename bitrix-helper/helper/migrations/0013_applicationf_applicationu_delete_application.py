# Generated by Django 4.2.6 on 2024-03-13 14:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0012_remove_pricelistfiz_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicationf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=50, verbose_name='Номер заявки')),
                ('name', models.TextField(null=True, verbose_name='Название заявки')),
                ('comment', models.TextField(null=True, verbose_name='Примечание')),
                ('participants', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
                ('pricelistFiz', models.ManyToManyField(blank=True, to='helper.pricelistfiz', verbose_name='Пункты прайслиста физические лица')),
            ],
            options={
                'verbose_name': 'Заявка ю.л',
                'verbose_name_plural': 'Заявки ю.л',
            },
        ),
        migrations.CreateModel(
            name='Applicationu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=50, verbose_name='Номер заявки')),
                ('name', models.TextField(null=True, verbose_name='Название заявки')),
                ('comment', models.TextField(null=True, verbose_name='Примечание')),
                ('participants', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
                ('pricelistFiz', models.ManyToManyField(blank=True, to='helper.pricelistfiz', verbose_name='Пункты прайслиста физические лица')),
            ],
            options={
                'verbose_name': 'Заявка ф.л',
                'verbose_name_plural': 'Заявки ф.л',
            },
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]
