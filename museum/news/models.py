from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Слаг', unique=True, allow_unicode=True)
    body = models.TextField('Текст новости')
    image = models.ImageField('Изображение', upload_to='news/', blank=True, null=True)
    published_at = models.DateTimeField('Дата публикации', auto_now_add=True)
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_at']

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})