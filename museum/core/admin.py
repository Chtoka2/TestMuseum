from django.contrib import admin
from .models import MuseumInfo

@admin.register(MuseumInfo)
class MuseumInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Запрещаем добавление, если запись уже есть
        return not MuseumInfo.objects.exists()