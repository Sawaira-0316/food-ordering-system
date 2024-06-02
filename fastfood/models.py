from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.IntegerField()
    priceL = models.IntegerField()
    pImage = models.URLField()

    def __str__(self):
        return self.name
    
class Burger(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.IntegerField()
    priceL = models.IntegerField()
    pImage = models.URLField()

    def __str__(self):
        return self.name
