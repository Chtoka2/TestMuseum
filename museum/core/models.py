from django.db import models

class MuseumInfo(models.Model):
    name = models.CharField('Название музея', max_length=200, default='Музей школы 22')
    description = models.TextField('Описание музея', blank=True)

    class Meta:
        verbose_name = 'Информация о музее'
        verbose_name_plural = 'Информация о музее'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Гарантируем, что всегда будет только одна запись
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        """Возвращает единственный экземпляр модели (создаёт, если его нет)."""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj