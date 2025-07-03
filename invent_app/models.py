from django.db import models

# Create your models here.
class Item(models.Model): 
 CATEGORY_CHOICES = [ 
        ('Electronics', 'Electronics'), 
        ('Furniture', 'Furniture'), 
        ('Stationery', 'Stationery'), 
        ('Clothing', 'Clothing'), 
        ('Food', 'Food'), 
        ('Other', 'Other'), 
    ] 
 
 name = models.CharField(max_length=100) 
 description = models.TextField(blank=True, null=True) 
 category = models.CharField(max_length=50, 
 choices=CATEGORY_CHOICES, default='Other') 
 quantity = models.PositiveIntegerField() 
 price = models.DecimalField(max_digits=10, decimal_places=2) 
 added_on = models.DateTimeField(auto_now_add=True)
