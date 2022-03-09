from django.db import models
from datetime import date

from django.urls import reverse

class Visitor(models.Model):
    ip = models.CharField("IP-адрес", max_length=15, default="")
    blocked = models.BooleanField("Заблокирован", default=False)
    reason = models.TextField("Причина блокировки", default="Чист")
    block_date = models.DateTimeField("Дата блокировки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Посетитель"
        verbose_name_plural = "Посетители"
