from django.contrib import admin
from .models import info
class infoAdmin(admin.ModelAdmin):
    list_display=['name','department','year']
# Register your models here.
admin.site.register(info,infoAdmin)