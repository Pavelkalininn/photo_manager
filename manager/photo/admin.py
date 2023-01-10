from django.contrib import (
    admin,
)
from django.contrib.admin import (
    ModelAdmin,
)
from photo.models import (
    Face,
    Photo,
)

admin.site.empty_value_display = '-пусто-'


class PhotoAdmin(ModelAdmin):
    list_display = (
        'id',
        'image',
        'gps_latitude',
        'gps_longitude',
        'date',
        'description',
    )
    search_fields = (
        'gps_latitude',
        'gps_longitude',
        'names',
        'date',
        'description',
    )
    list_filter = (
        'gps_latitude',
        'gps_longitude',
        'names',
        'date',
        'description',
    )


class FaceAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )


admin.site.register(Face, FaceAdmin)
admin.site.register(Photo, PhotoAdmin)
