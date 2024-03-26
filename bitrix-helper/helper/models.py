from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.core.validators import MaxValueValidator , MinValueValidator

class Department(models.Model):
    name = models.TextField(null=True, blank=False,verbose_name='Название группы/отдела')
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Группы/отделы'
        verbose_name = 'Группа/отдел'


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,verbose_name='Прошел активацию?')
    department = models.ForeignKey(Department,null=True,blank=True, verbose_name='Группа/отдел',on_delete = models.CASCADE)
    
    class Meta(AbstractUser.Meta):
        pass

class PriceListFiz(models.Model):
    num = models.CharField(null=False,blank=False,max_length=50,verbose_name='Номер услуги')
    name = models.TextField(null=True, blank=False,verbose_name='Название услуги')
    time = models.CharField(null=False,blank=False,max_length=50,verbose_name='Срок выполнения')
    comment = models.TextField(null=True, blank=True,verbose_name='Примечание')
    department = models.ForeignKey(Department,null=True,blank=True, verbose_name='Группа/отдел',on_delete = models.CASCADE)
    price = models.FloatField(null=True,blank=False, validators=[MinValueValidator(0)],verbose_name='Цена')

    def __str__(self):
        return f'{self.num,self.name}'

    class Meta:
        verbose_name_plural = 'Прайс физические лица'
        verbose_name = 'Прайс физические лица'

class PriceListUr(models.Model):
    sec=(
        ('1','1.Санитарно-гигиенические услуги'),
        ('1a','1A.Санитарно-гигиенические услуги-административные процедуры'),
        ('2','2.Отбор проб, органолептические и физико-химические (санитарно-химические) исследования объектов окружающей среды'),
        ('3','3.Физико-химические и инструментальные исследования и испытания продукции'),
        ('4','4.Измерения (исследования) физических факторов окружающей и производственной среды'),
        ('5','5.Радиологические исследования и измерения'),
        ('6','6.Микробиологические исследования'),
        ('7','7.Токсикологические, биохимические и гематологические исследования'),
        ('8','8.'),
        ('san','Санитарно-эпидемиологические услуги для нерезидентов'),
        ('9','9.Административные процедуры, осуществляемые в отношении субъектов хозяйствования'),
        ('test','Тестирование на инфекцию COVID-19 методом ПЦР в режиме реального времени'),
        )
    num = models.CharField(null=False,blank=False,max_length=50,verbose_name='Номер услуги')
    name = models.TextField(null=True, blank=False,verbose_name='Название услуги')
    ed = models.CharField(null=False,blank=False,max_length=50,verbose_name='Единица измерения')
    comment = models.TextField(null=True, blank=True,verbose_name='Примечание')
    department = models.ForeignKey(Department,null=True,blank=True, verbose_name='Группа/отдел',on_delete = models.CASCADE)
    section = models.CharField(null=True, blank=False, choices=sec,max_length=50, verbose_name='Раздел')
    price_first = models.FloatField(null=True,blank=False, validators=[MinValueValidator(0)],verbose_name='Тариф без НДС - единичное')
    priceNDS_first = models.FloatField(null=True,blank=False, validators=[MinValueValidator(0)],verbose_name='Тариф с НДС - единичное')
    price_next = models.FloatField(null=True,blank=False, validators=[MinValueValidator(0)],verbose_name='Тариф без НДС - последующее')
    priceNDS_next = models.FloatField(null=True,blank=False, validators=[MinValueValidator(0)],verbose_name='Тариф с НДС - последующее')

    def __str__(self):
        return f'{self.num,self.name}'

    class Meta:
        verbose_name_plural = 'Прайс юридические лица'
        verbose_name = 'Прайс юридические лица'

class Applicationf(models.Model):
    num = models.CharField(null=False,blank=False,max_length=50,verbose_name='Номер заявки')
    name = models.TextField(null=True, blank=False,verbose_name='Название заявки')
    comment = models.TextField(null=True, blank=False,verbose_name='Примечание')
    participants = models.ManyToManyField(AdvUser,blank=True, verbose_name='Участники')
    pricelistFiz = models.ManyToManyField(PriceListFiz,blank=True, verbose_name='Пункты прайслиста физические лица')
    is_active = models.BooleanField(default=True, db_index=True,verbose_name='Активная заявка')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Заявки ф.л'
        verbose_name = 'Заявка ф.л'


class Applicationu(models.Model):
    num = models.CharField(null=False,blank=False,max_length=50,verbose_name='Номер заявки')
    name = models.TextField(null=True, blank=False,verbose_name='Название заявки')
    comment = models.TextField(null=True, blank=False,verbose_name='Примечание')
    participants = models.ManyToManyField(AdvUser,blank=True, verbose_name='Участники')
    pricelistUr = models.ManyToManyField(PriceListUr,blank=True, verbose_name='Пункты прайслиста физические лица')
    is_active = models.BooleanField(default=True, db_index=True,verbose_name='Активная заявка')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Заявки ю.л'
        verbose_name = 'Заявка ю.л'