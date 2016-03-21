from django.contrib import admin
from django.db import models
from models import Asset, Category, MediaImage, MediaVoiceMemo, Type, Location

class MediaImageInline(admin.StackedInline):
    fieldsets = (
        (
            None,
            {
                'fields': ('image', 'thumbnail')
            }
        ),
    )
    readonly_fields = ('thumbnail',)
    model = MediaImage
    extra = 0

class MediaVoiceMemoInline(admin.StackedInline):
    fieldsets = (
        (
            None,
            {
                'fields': ('voice_memo',)
            }
        ),
    )
    model = MediaVoiceMemo
    extra = 0

class LocationInline(admin.StackedInline):
    model = Location
    extra = 1
    max_num = 1

class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'asset_type',)
    fieldsets = (
        (None, {'fields': ('name', 'description', 'category', 'asset_type')}),
    )
    inlines = (MediaImageInline, MediaVoiceMemoInline, LocationInline, )



admin.site.register(Asset, AssetAdmin)
# admin.site.register(Media)
admin.site.register(Category)
admin.site.register(Type)
# admin.site.register(Location)