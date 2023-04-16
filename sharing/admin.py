from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from sharing.models import *


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'number', 'capacity', 'image', 'drive_count')
    list_display_links = ('id', 'name', 'number', 'capacity')
    search_fields = ('name', 'number', 'description')
    list_filter = ('category', 'capacity', 'color', 'brand')
    autocomplete_fields = ('category', 'color', 'brand')
    readonly_fields = ('drive_count',)

    def drive_count(self, obj):
        return Drive.objects.filter(vehicle_id=obj.pk).count()

    drive_count.short_description = 'Количество поездок'

    def image(self, obj):
        if obj.photo:
            return mark_safe(f'<img height="200px" src="/media/{obj.photo}" />')
        return 'Без фотографии'

    image.short_description = 'Фотография'


class BikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'brand', 'color', 'drive_count', 'photo')
    list_display_links = ('id', 'name', 'price', 'brand', 'color')
    search_fields = ('name', 'color', 'description')
    list_filter = ('category', 'color', 'brand')
    autocomplete_fields = ('category', 'color', 'brand')
    readonly_fields = ('drive_count',)

    def drive_count(self, obj):
        return Drive.objects.filter(bike_id=obj.pk).count()

    drive_count.short_description = 'Количество поездок'

    def image(self, obj):
        if obj.photo:
            return mark_safe(f'<img height="200px" src="{obj.photo}" />')
        return 'Без фотографии'

    image.short_description = 'Фотография'


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class DriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver', 'status', 'rating', 'date')
    list_display_links = ('id', 'driver', 'status', 'rating', 'date')
    search_fields = ('driver', 'vehicle', 'bike')
    list_filter = ('date', 'status')
    autocomplete_fields = ('driver', 'vehicle', 'bike')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date')
    list_display_links = ('id', 'email', 'date')
    search_fields = ('email', 'subject')
    list_filter = ('date',)
    autocomplete_fields = ('user',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'excerpt', 'author', 'image', 'created_at')
    list_display_links = ('id', 'title', 'excerpt')
    search_fields = ('title', 'excerpt', 'content')
    list_filter = ('created_at',)
    autocomplete_fields = ('author',)

    def image(self, obj):
        if obj.preview:
            return mark_safe(f'<img height="200px" src="{obj.preview}" />')
        return 'Без изображения'

    image.short_description = 'Изображение'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Drive, DriveAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Bike, BikeAdmin)
