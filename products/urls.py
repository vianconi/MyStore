from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.index),
    path('products/<int:product_id>/detail', views.detail, name='detail'),
    path('products/category/<int:category_id>', views.get_products_by_category, name='category'),
]