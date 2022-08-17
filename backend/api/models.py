from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    last_price = models.CharField(max_length=100)
    changed_value = models.CharField(max_length=100)
    volume = models.CharField(max_length=200)

    def __str__(self):
        return self.name
