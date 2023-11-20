from django.db import models
# Testing DB creation by using Django Models
# Create your models here.
class StockData(models.Model):
    volume = models.IntegerField()
    ticker = models.CharField(max_length=10)
    date = models.DateField()
    open = models.FloatField()
    open_price = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    
def __str__(self):
    return f"{self.ticker} - {self.date}"
