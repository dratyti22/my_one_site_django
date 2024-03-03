from django.db import models

# Create your models here.


class Index(models.Model):
    content = models.TextField(verbose_name="Текст приветствия")

    class Meta:
        db_table = "index"
        verbose_name = "Главная"
        verbose_name_plural = "Главная"


class About(models.Model):
    text_on_page = models.TextField(verbose_name="Текст о нас")
    content = models.TextField(verbose_name="Текст")

    class Meta:
        db_table = "about"
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class Contact(models.Model):
    heading = models.CharField(max_length=150, verbose_name="Заголовок")
    informarion = models.TextField(verbose_name="Текст про контакты")

    class Meta:
        db_table = 'contact'
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
