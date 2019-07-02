from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Автор")

    class Meta():
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название книги")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name="Автор книги")
    year = models.PositiveIntegerField(blank=True, null=True, verbose_name="Год издания")

    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
