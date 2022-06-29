from django.utils import timezone
#rest
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from producto.models import Product
#models
from .models import Sale,SaleDetail
#serializer
from .serializers import (
    ReportSaleSerializer,
    ProccessSailSerializer,
    ProccessSailSerializer2,
)

# Create your views here.

class ListReportSales(ListAPIView):
    serializer_class = ReportSaleSerializer

    def get_queryset(self):
        return Sale.objects.all()

#With craeteApiView we actumatilly create a form
class RegisterSail(CreateAPIView):
    #permission
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = ProccessSailSerializer

    #we are overwriting a method of the class
    def create(self,request,*args,**kwargs):
        #we recieved the data from the class and then...
        serializer = ProccessSailSerializer(data=request.data)
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
        products = serializer.validated_data['products']
        #iterate or use bulk
        detail_sale = []
        for prod in products:
            #find the product, then create a saleDetail 
            product = Product.objects.get(id=prod['pk'])
            sale_detail = SaleDetail(
                sale=venta,
                product=product,
                count=prod['count'],
                price_purchase= product.price_purchase,
                price_sale = product.price_sale,
            )
            amount = amount + product.price_purchase*prod['count']
            count = count + prod['count']
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

#the same thing in a good way
class RegisterSail2(CreateAPIView):
    #permission
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = ProccessSailSerializer

    #we are overwriting a method of the class
    def create(self,request,*args,**kwargs):
        #we recieved the data from the class and then...
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