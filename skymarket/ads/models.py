from django.conf import settings
from django.db import models
from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name="Объявление")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return f"{self.title} - {self.author}({self.created_at})"

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст отзыва")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return f"{self.author}({self.created_at})"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
