from django.db import models

# Create your models here.

class StockData(models.Model):
    symbol = models.CharField(max_lengght= 10)
    date = models.DateField()                 # Date of the stock data

    open_price = models.DecimalField(max_digits=10, decimal_places=2)

    close_price = models.DecimalField(max_digits=10, decimal_places=2)

    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()         # Trading volume