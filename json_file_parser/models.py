from django.db import models


class FileJson(models.Model):
    """Модель для записей из json"""
    name = models.CharField('Имя', max_length=49)
    date = models.DateTimeField()
