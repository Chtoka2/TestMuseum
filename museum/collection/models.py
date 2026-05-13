from django.db import models

class Exhibit(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    approximate_year = models.CharField('Примерный год', max_length=100, blank=True,
                                        help_text='Например: 1943, 1970-е, начало XX века')
    category = models.CharField('Тип экспоната', max_length=100, blank=True,
                                help_text='Например: самолёт, жетон, фляга, костюм')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Экспонат'
        verbose_name_plural = 'Экспонаты'
        ordering = ['title']

    def __str__(self) -> str:
        return str(self.title)


class ExhibitImage(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Изображение', upload_to='exhibits/')
    caption = models.CharField('Подпись', max_length=200, blank=True)
    order = models.PositiveSmallIntegerField('Порядок', default=0) # type: ignore

    class Meta:
        verbose_name = 'Фотография экспоната'
        verbose_name_plural = 'Фотографии экспонатов'
        ordering = ['order', 'id']

    def __str__(self) -> str:
        return f"Фото для {str(self.exhibit.title)}" # type: ignore