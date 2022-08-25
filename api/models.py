from django.db import models
from django.utils import timezone
from .behaviours import StatusMixin,UUIDMixin

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField( max_length=100, null=True)
    age = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description=models.TextField(null=True)
    selling_price=models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Stock(models.Model):
    units = models.IntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.units



class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    total=models.IntegerField(default=0)
    mobile=models.IntegerField()
    product = models.ManyToManyField(Product,blank=True)
    
    def __str__(self):
        return "Order:" + str(self.id)