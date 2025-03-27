from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    description = models.CharField(max_length=200)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    image = models.ImageField(null=True, blank=True, upload_to='media/products')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} | {self.price}'


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    discount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    
