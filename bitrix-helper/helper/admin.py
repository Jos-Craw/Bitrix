from django.contrib import admin
import datetime

from .models import AdvUser, Application, PriceList


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id','num','name')
    list_display_links = ('num','name',)
    search_fields = ('num','name')
    fields = ('num','name','comment','participants','pricelist',)


admin.site.register(Application, ApplicationAdmin)



class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','first_name', 'last_name','department')
    list_display_links = ('username',)
    search_fields = ('username', 'first_name', 'last_name','department',)
    fields = ('username',('first_name', 'last_name'), ('is_staff', 'is_superuser'),'department', 'user_permissions',)


admin.site.register(AdvUser, AdvUserAdmin)



class PriceAdmin(admin.ModelAdmin):
    list_display = ('id','num','name','comment','department','price')
    list_display_links = ('name',)
    search_fields = ('num','name',)
    fields = ('num','name','comment','department','price',)


admin.site.register(PriceList, PriceAdmin)