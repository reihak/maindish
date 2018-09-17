from django.contrib import admin
from .models import Menu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'food_stuff', 'name', 'link', 'text', 'updated_datetime')
    list_display_links = ('id', 'title', 'food_stuff', 'name', 'link', 'text')

admin.site.register(Menu, MenuAdmin)
