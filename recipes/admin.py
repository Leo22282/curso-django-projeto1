from django.contrib import admin

from .models import Category

# Register your models here.
#Aqui você informa as tabelas que aparecem no http://127.0.0.1:8000/admin

class CategoryAdmin(admin.ModelAdmin):
    ...
    
admin.site.register(Category, CategoryAdmin)