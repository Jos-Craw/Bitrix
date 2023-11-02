from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
from .utilities import send_activation_notification
import os
from django.core.validators import MaxValueValidator , MinValueValidator

class AdvUser(AbstractUser):
    dep=(
        ('adm','Администратор'),
        ('emp','Группа акустики и ЭМП'),
        )
    is_activated = models.BooleanField(default=True, db_index=True,verbose_name='Прошел активацию?')
    department = models.CharField(null=True, blank=False, choices=dep,max_length=50, verbose_name='Группа')
    

    class Meta(AbstractUser.Meta):
        pass


class Application(models.Model):
    num = models.CharField(null=False,blank=False,max_length=50,verbose_name='Номер заявки')
    name = models.TextField(null=True, blank=False,verbose_name='Название заявки')
    comment = models.TextField(null=True, blank=False,verbose_name='Примечание')
    participants = models.ManyToManyField(AdvUser,blank=True, verbose_name='Участники')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'Заявка'

class PriceList(models.Model):
    num = models.CharField(null=False,blank=False,max_length=50,verbose_name='Номер услуги')
    name = models.TextField(null=True, blank=False,verbose_name='Название услуги')
    comment = models.TextField(null=True, blank=False,verbose_name='Примечание')


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Прайс'
        verbose_name = 'Прайс'




user_registrated = Signal(['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)