from django.db import models


# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now = True)
    date_updated = models.DateTimeField(auto_now= True)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ['date_created']
