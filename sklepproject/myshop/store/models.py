from django.db import models
from django.utils import timezone


class Clothing(models.Model):
    type = models.CharField(max_length=100,default="Brak informacji")
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    size = models.FloatField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.description


class Rates(models.Model):
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE, null=True)
    rate=models.IntegerField()
    opinion=models.CharField(max_length=300)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.clothing.name} - {self.date_created}'
