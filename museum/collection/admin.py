from django.contrib import admin
from django.utils.html import format_html
from .models import Exhibit, ExhibitImage

class ExhibitImageInline(admin.TabularInline):
    model = ExhibitImage
    extra = 1
    fields = ['image', 'caption', 'order', 'image_preview']
    readonly_fields = ['image_preview']

    @admin.display(description='Превью')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:5px;" />', obj.image.url)
        return "—"


@admin.register(Exhibit)
class ExhibitAdmin(admin.ModelAdmin):
    # Поля в списке экспонатов
    list_display = ['title', 'category', 'approximate_year', 'main_image_preview']
    list_filter = ['category']
    search_fields = ['title', 'description']

    # Группировка полей в форме редактирования
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'approximate_year')
        }),
        ('Описание', {
            'fields': ('description',),
            'classes': ('wide',)
        }),
        ('Главное изображение (первое из галереи)', {
            'fields': ('main_image_display',),
            'description': 'Чтобы сменить главное фото, измените порядок в галерее ниже.'
        }),
    )
    readonly_fields = ['main_image_display']

    # Встроенная галерея фотографий
    inlines = [ExhibitImageInline]

    # Методы для отображения картинок
    @admin.display(description='Фото')
    def main_image_preview(self, obj):
        """Миниатюра для списка экспонатов"""
        first_image = obj.images.first()
        if first_image and first_image.image:
            return format_html('<img src="{}" width="60" style="border-radius:5px;" />', first_image.image.url)
        return "—"

    @admin.display(description='Текущее главное фото')
    def main_image_display(self, obj):
        """Большое превью в форме редактирования"""
        first_image = obj.images.first()
        if first_image and first_image.image:
            return format_html('<img src="{}" width="300" style="border-radius:10px;" />', first_image.image.url)
        return "Главное фото не задано. Загрузите фотографии в галерее ниже и установите порядок."