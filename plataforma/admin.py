from django.contrib import admin

from plataforma import models

admin.site.register(models.Post)
admin.site.register(models.Category)
admin.site.register(models.Comment)
