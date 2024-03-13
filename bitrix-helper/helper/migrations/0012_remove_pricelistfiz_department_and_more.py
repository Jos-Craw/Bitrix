# Generated by Django 4.2.6 on 2024-03-13 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0011_remove_advuser_department_advuser_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricelistfiz',
            name='department',
        ),
        migrations.RemoveField(
            model_name='pricelistur',
            name='department',
        ),
        migrations.AddField(
            model_name='pricelistfiz',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helper.department', verbose_name='Группа/отдел'),
        ),
        migrations.AddField(
            model_name='pricelistur',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helper.department', verbose_name='Группа/отдел'),
        ),
    ]