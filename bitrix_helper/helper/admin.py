from django.contrib import admin
import datetime

from .models import AdvUser, Application

class AppAdmin(admin.ModelAdmin):
    list_display = ('id','num','name', 'content', 'author', 'pubdate', 'file')
    list_display_links = ('content','name',)
    search_fields = ('num','name','content', 'author', 'file')
    date_hierarchy = 'pubdate'
    fields = ('num','name','author', 'content','file')

admin.site.register(Application, AppAdmin)