from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.api import viewsets

urlpatterns = [
    path('latest-products/', viewsets.LatestProductsList.as_view()),
    path('products/search/', viewsets.search),
    path('products/<slug:category_slug>/<slug:product_slug>/',
         viewsets.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', viewsets.CategoryDetail.as_view()),
]
