from django.db import models

# Create your models here.
class Item(models.Model):
    """Товар/Продукт"""
    name = models.CharField('Название', max_length=300)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name