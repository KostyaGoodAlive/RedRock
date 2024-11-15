from django.contrib import admin
from .models import NewsCard, ClubsCard, Photo,LocationsCard
from .models import CarouselImage, Team08_09


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('caption_title', 'order')
    ordering = ('order',)

@admin.register(Team08_09)
class Team08_09Admin(admin.ModelAdmin):
    list_display = ('full_name', 'trainer', 'ppg')
    search_fields = ('full_name', 'trainer')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'uploaded_at')
    search_fields = ('description',)

admin.site.register(LocationsCard)
admin.site.register(NewsCard)
admin.site.register(ClubsCard)
