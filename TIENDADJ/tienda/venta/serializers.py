#
from rest_framework import serializers
#models
from .models import Sale, SaleDetail

class ReportSaleSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    #serializer to see the detail sales
    class Meta:
        model = Sale
        fields = (
            'id',
            'date_sale',
            'amount',
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send',
            'anulate',
            'user',
            'products',
        )
    """
    As form we declared a SerializerMethodField where this call his function and recieved each obj and
    we can return some calcuos.

    In this case we return a sale and a sale can have a list of products that were bought 
    """
    def get_products(self,obj):
        query = SaleDetail.objects.products_per_sale(obj.id)
        products_serializers = DetailSaleProductSerializer(query,many=True).data
        return products_serializers
#
class DetailSaleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = SaleDetail
        fields = (
            'id',
            'sale',
            'product',
            'count',
            'price_purchase',
            'price_sale'
        )
#
class ProductDetailSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    count = serializers.IntegerField()

class ProccessSailSerializer(serializers.Serializer):
    type_invoce = serializers.CharField()      
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    products = ProductDetailSerializer(many=True)

#we are going to do the same but in a good way
class ArrayIntegerSerializer(serializers.ListField):
    child = serializers.IntegerField()


class ProccessSailSerializer2(serializers.Serializer):
    type_invoce = serializers.CharField()      
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    products = ArrayIntegerSerializer()
    counts = ArrayIntegerSerializer()

    #validate 
    #Value contain the value that was choosen at that time
    def validate_type_invoce(self, value):
        if value != '0':
            raise serializers.ValidationError('Ingresse un valor correcto')
        return value
    #another and is global
    #Data contain all the values inside a dictionary
    def validate(self, data):
        if data['type_payment'] != '0':
            raise serializers.ValidationError('Ingresse un tipo de pago')
