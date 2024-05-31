from django.contrib import admin
from .models import City


class cityAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


# Register your models here.
admin.site.register(City, cityAdmin)
