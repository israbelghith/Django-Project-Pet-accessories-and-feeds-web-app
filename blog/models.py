from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=50)
    desc=models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image=models.ImageField(null=True,blank=True)
   # category=models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
# Create your models here.

class Product(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=50)
    desc=models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image=models.ImageField(null=True,blank=True)
   # category=models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
