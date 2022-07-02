
from rest_framework import serializers, pagination
#
from .models import Product, Colors

class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = (
            'color',
        )

#pagination
class ProductPagination(pagination.PageNumberPagination):
    page_size = 2
    max_page_size=1

class ProductSerializer(serializers.ModelSerializer):

    colors = ColorsSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'man',
            'woman',
            'weight',
            'price_purchase',
            'price_sale',
            'main_image',
            'image1',
            'image2',
            'image3',
            'image4',
            'colors',
            'video',
            'stok',
            'num_sales',
            'user_created',
        )
class ProductSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')