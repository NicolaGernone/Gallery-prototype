from django.contrib import admin

from .models import *


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'url', 'created_at')

@admin.register(Event)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields=('user_id', 'image_id', 'click', 'view', 'weight', 'updated_at')
    list_display=('user_id', 'image_id', 'click', 'view', 'weight', 'updated_at')

admin.site.register(Category)
    