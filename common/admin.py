from django.contrib import admin
from bot import models

admin.site.register(models.TelegramUser)
admin.site.register(models.TelegramChannel)
admin.site.register(models.TelegramAdmin)
admin.site.register(models.Image)
admin.site.register(models.ImageGroup)
