from django.db import models
from django.conf import settings
from datetime import datetime as dt


# Create your models here.
class Inventory(models.Model):
    item =models.CharField(primary_key=True, max_length=50)
    amount_on_hand =models.IntegerField(default=0)
    unit_measure = models.CharField(null = False, max_length=50)
    cost_uom =models.FloatField(null=False)

    def update_qty(self, amount):
        self.amount_on_hand+= amount
        self.save()
    
    def __str__(self):
        return f'{self.item} {self.amount_on_hand} {self.unit_measure}'

class Sales(models.Model):
    transaction_id =models.BigIntegerField(primary_key=True)
    total_amount= models.FloatField(null =False)
    dt =models.DateTimeField(default= dt.now)

    def __str__(self):
        return f'{self.transaction_id} for {self.total_amount} on {self.dt}'

class Menue_Item(models.Model):
    entree =models.CharField(primary_key =True, max_length=50)
    price =models.FloatField(null=False)
    created_by =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.entree} priced at {self.price}'

class Recipe_list(models.Model):
    entree =models.ForeignKey(Menue_Item, on_delete =models.CASCADE)
    inventory =models.ForeignKey(Inventory, on_delete = models.CASCADE)
    recipe_amount_used = models.FloatField(null=False)

    def __str__(self):
        return f'{self.entree} {self.inventory}'


class SalesLines(models.Model):
    transaction_id= models.ForeignKey(Sales, on_delete =models.CASCADE)
    entree =models.ForeignKey(Inventory, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.transaction_id} item {self.entree}'
