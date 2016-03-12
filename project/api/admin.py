from django.contrib import admin
from django.db import models
from models import Asset, Category, Media, Type, Location

class MediaInline(admin.StackedInline):
    fieldsets = (
        (
            None,
            {
                'fields': ('voice_memo', 'image', 'thumbnail')
            }
        ),
    )

    readonly_fields = ('thumbnail',)
    model = Media
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
    inlines = (MediaInline, LocationInline, )



admin.site.register(Asset, AssetAdmin)
# admin.site.register(Media)
admin.site.register(Category)
admin.site.register(Type)
# admin.site.register(Location)