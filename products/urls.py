from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CategoryListView,
    CategoryDetailView,
    related_products
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/<int:product_id>/related/', related_products, name='related-products'),
]
