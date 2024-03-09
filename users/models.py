from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True,verbose_name="Аватар")
    phone_number = models.CharField(max_length=10, null=True, blank=True,verbose_name="Номер телефона")

    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username
