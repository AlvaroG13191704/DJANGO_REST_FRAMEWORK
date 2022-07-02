from django.utils import timezone
from django.shortcuts import get_object_or_404
#
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
#
from ..serializers import ProccessSailSerializer2,ReportSaleSerializer
#
from ..models import Sale, SaleDetail
#
from producto.models import Product

"""
This throws an error 404
Viewset works so diferent instead of ModelViewSet, because Model knows what model use to work
In ViewSet we need to override their functions, and 

"""
class SaleViewSet(viewsets.ViewSet):

    authentication_classes = (TokenAuthentication,)
    # 
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve' :
            permission_classes = [AllowAny]
        else :
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = Sale.objects.all()
        serializer = ReportSaleSerializer(queryset,many=True)
        return Response(serializer.data)
    #get one sale
    def retrieve(self, request, pk=None):
        sale = get_object_or_404(Sale,pk=pk)
        serializer = ReportSaleSerializer(sale)
        return Response(serializer.data)
    #update
    def update(self, request, pk=None):
        sale = Sale.objects.get(id=pk)
        serializer = ProccessSailSerializer2(sale)
        return Response(serializer.data)
    #create only works with POST method
    def create(self, request):
        
        serializer = ProccessSailSerializer2(data=request.data)
        #We need to valid the data
        serializer.is_valid(raise_exception=True)
        #this is a value
        type_invoce = serializer.validated_data['type_invoce']
        #save
        venta = Sale.objects.create(
            date_sale=timezone.now(),
            amount= 0,
            count=0,
            type_invoce=serializer.validated_data['type_invoce'],
            type_payment=serializer.validated_data['type_payment'],
            adreese_send=serializer.validated_data['adreese_send'],
            user=self.request.user
        ) 
        #variables to update
        amount = 0
        count = 0
        #get the sale products, this is a dictionary
        products = Product.objects.filter(
            id__in=serializer.validated_data['products']
        )
        counts = serializer.validated_data['counts']
        #iterate or use bulk
        detail_sale = []
        for prod,cont in zip(products,counts):
            #find the product, then create a saleDetail 
            sale_detail = SaleDetail(
                sale=venta,
                product=prod,
                count=cont,
                price_purchase= prod.price_purchase,
                price_sale = prod.price_sale,
            )
            amount = amount + prod.price_purchase*cont
            count = count + cont
            #store in the array
            detail_sale.append(sale_detail)

        #update the sale
        venta.amount = amount
        venta.count = count
        venta.save()
        #save the sales
        SaleDetail.objects.bulk_create(detail_sale)
         

        print(type_invoce)
        return Response({
            'code':'Venta exitosa'
        })