from django.contrib import admin
import datetime

from .models import AdvUser, Application, PriceListFiz, PriceListUr, Department


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id','num','name')
    list_display_links = ('num','name',)
    search_fields = ('num','name')
    fields = ('num','name','comment','participants','pricelistFiz','pricelistUr',)


admin.site.register(Application, ApplicationAdmin)



class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','first_name', 'last_name')
    list_display_links = ('username',)
    search_fields = ('username', 'first_name', 'last_name','department',)
    fields = ('username',('first_name', 'last_name'), ('is_staff', 'is_superuser'),'department', 'user_permissions',)


admin.site.register(AdvUser, AdvUserAdmin)



class PriceAdminFiz(admin.ModelAdmin):
    list_display = ('id','num','name','time','comment','price')
    list_display_links = ('name',)
    search_fields = ('num','name',)
    fields = ('num','name','time','comment','department','price',)


admin.site.register(PriceListFiz, PriceAdminFiz)

class PriceAdminUr(admin.ModelAdmin):
    list_display = ('id','num','name','ed','comment','price','priceNDS')
    list_display_links = ('name',)
    search_fields = ('num','name',)
    fields = ('num','name','ed','comment','department','price','priceNDS',)


admin.site.register(PriceListUr, PriceAdminUr)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('name',)
    search_fields = ('name',)
    fields = ('name',)


admin.site.register(Department, DepartmentAdmin)