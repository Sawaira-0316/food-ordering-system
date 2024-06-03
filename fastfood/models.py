from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=120)
    size= models.CharField(max_length=120 ,default="M")
    category = models.CharField(max_length=120 , default="Fajita")
    priceM = models.IntegerField()
    priceL = models.IntegerField()
    pImage = models.URLField()

    def __str__(self):
        return self.name
    
class Burger(models.Model):
    name = models.CharField(max_length=120)
    size = models.CharField(max_length=120, default="M")
    category = models.CharField(max_length=120 , default="Zinger")
    priceM = models.IntegerField()
    priceL = models.IntegerField()
    pImage = models.URLField(default='http://example.com/default-image.jpg')

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    orderBy = models.CharField(max_length=100)
    orderDateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name