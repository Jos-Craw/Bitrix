from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
import os


class AdvUser(AbstractUser):
	dep = (
		('emp','Группа измерения акустики и электромагнитных полей'),
		('doz','Группа дозиметрических'),
		)
		

	is_activated = models.BooleanField(default=True, db_index=True,verbose_name='Прошел активацию')
	Department = models.CharField(null = True, blank =False,choices=dep,max_length=50,verbose_name='Группа/отдел')
	name = models.CharField(null=True,blank=False,max_length=100,verbose_name='Имя')
	
	class Meta(AbstractUser.Meta):
		pass



class Application(models.Model):
	num = models.CharField(null=False, blank=False,max_length=100,verbose_name='Номер заявки')
	name = models.CharField(null=True, blank=False,max_length=100,verbose_name='Название заявки')
	content = models.TextField(null=True, blank=False,verbose_name='Контент')
	file = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, null=True,verbose_name='Приклепленные файлы')
	author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, null=True,verbose_name='Автор')
	pubdate = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата ')

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name_plural = 'Заявки'
		verbose_name = 'Заявка'
		ordering = ['pubdate']

	def filename(self):
		return os.path.basename(self.file.name)

user_registrated = Signal(['instance'])


def user_registrated_dispatcher(sender, **kwargs):
	send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)