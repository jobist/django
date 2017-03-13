from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название категории', unique=True, db_index = True)
    class Meta:        
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        db_table = 'category'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'products', )
    name = models.CharField(max_length = 250, verbose_name = 'Товар', db_index = True, unique = True)
    description = models.TextField()
    slug = models.SlugField(max_length=250, db_index=True)
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'products'