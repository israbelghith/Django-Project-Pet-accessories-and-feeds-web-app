from django.contrib import admin
from .models import Article
from .models import Category
from .models import Product

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Product)
# Register your models here.
