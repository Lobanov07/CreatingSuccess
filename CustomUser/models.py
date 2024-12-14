from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name="О себе"
    )  # Дополнительное поле для описания пользователя
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения"
    )  # Поле для даты рождения
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True,
        verbose_name="Фото профиля"
    )  # Фото профиля
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Номер телефона"
    )  # Телефонный номер
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Профиль создан"
    )  # Дата создания профиля
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Профиль обновлен"
    )  # Дата последнего обновления профиля

    def __str__(self):
        return self.username  # Вывод имени пользователя

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "пользователи"
