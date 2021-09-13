from rest_framework import serializers

from product.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'get_absolute_url',
                  'description', 'price', 'get_image', 'get_thumbnail']


class CategorySerializer(serializers.ModelSerializer):
    # hien thi products khi request category, neu khong co chi hien ra id
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'get_absolute_url', 'products']
