from django.db import models
from django.contrib.auth.models import User
class Category(models.TextChoices):
    ELECTRONICS="Electronics"
    LAPTOPS="Laptops"
    ARTS="Arts"
    FOOD="Food"
    HOME="Home"
    KITCHEN="Kitchens"
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True,default="")
    description= models.TextField(max_length=1000,default="",blank=False)
    price=models.DecimalField(max_digits=7,decimal_places=2,default=0)
    brand=models.CharField(max_length=100,blank=False,null=True,default="")
    category=models.CharField(max_length=30,choices=Category.choices)
    ratings=models.DecimalField(max_digits=3,decimal_places=2,default=0)
    stock = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name