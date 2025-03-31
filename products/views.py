from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Product, Category

# Create your views here.
def index(request):
    products = Product.objects.select_related('category').all()

    context = {
        'products': products
    }

    return render(request, 'products/index.html', context)

@login_required
def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }

    return render(request, 'products/detail.html', context)

def get_products_by_category(request, category_id):
    category = Category.objects.prefetch_related('products').get(id=category_id)
    products = category.products.all()

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'products/category.html', context)