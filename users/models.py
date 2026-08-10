from django.db import models

# Create your modclass Medicine(models.Model):
from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    store_name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        