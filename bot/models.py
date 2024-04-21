from django.db import models
from common.models import BaseModel


class LanguageChoices(models.TextChoices):
    RUSSIAN = "ru", "Russian"
    UZBEK = "uz", "Uzbek"


class TelegramChannel(BaseModel):
    chat_id = models.BigIntegerField(unique=True)

    language = models.CharField(
        max_length=2, choices=LanguageChoices.choices, null=True, blank=True
    )

    def __str__(self):
        return f"{self.chat_id}"


class TelegramUser(BaseModel):
    chat_id = models.PositiveIntegerField(unique=True)

    language = models.CharField(
        max_length=2, choices=LanguageChoices.choices, null=True, blank=True
    )

    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.chat_id} {self.first_name}"


class TelegramAdmin(BaseModel):
    chat_id = models.PositiveIntegerField(unique=True)

    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.chat_id}"


class ImageGroup(BaseModel):
    language = models.CharField(max_length=2, choices=LanguageChoices.choices)


class Image(BaseModel):
    image_group = models.ForeignKey(
        ImageGroup, on_delete=models.CASCADE, related_name="images"
    )

    file_id = models.CharField(max_length=255)
    content_type = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.file_id}"
