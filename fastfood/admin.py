from django.contrib import admin
from .models import Pizza,Burger


# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
 list_display = ('name', 'priceL', 'priceM')

admin.site.register(Pizza ,PizzaAdmin)


class BurgerAdmin(admin.ModelAdmin):
 list_display = ('name', 'priceL', 'priceM')

admin.site.register(Burger,BurgerAdmin)