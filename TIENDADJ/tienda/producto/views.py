from django.shortcuts import render
#rest
from rest_framework.generics import (
    ListAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#
from .serializers import ProductSerializer
#mopdels
from .models import Product
# Create your views here.

#
class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer
    #This identify and authtenticated the user  
    authentication_classes = (TokenAuthentication,)
    #This view can be charged if the permissions are correct
    permission_classes = [IsAuthenticated]
    #func
    def get_queryset(self):
        user = self.request.user
        return Product.objects.products_per_user(user)
#
class ListProductStok(ListAPIView):
    serializer_class = ProductSerializer
    """
    With auth_class we only verified if a token was sent, if wasn't nothning happends and the
    url still working, this is dangerous, So we need to use the permission_class to allow the view to work
    """
    authentication_classes = (TokenAuthentication,)
    #This view can be charged if the permissions are correct
    #permission_classes = [IsAuthenticated,IsAdminUser]
    #func
    def get_queryset(self):
        return Product.objects.products_w_stok()
#
class ListProductGender(ListAPIView):
    serializer_class = ProductSerializer
    #func
    def get_queryset(self):
        user = self.request.user
        #get a parameter from the url
        gender = self.kwargs['gender']
        return Product.objects.products_b_gender(gender)

#
class FilterProducts(ListAPIView):
    serializer_class = ProductSerializer
    #
    def get_queryset(self):
        man= self.request.query_params.get('man',None)
        woman= self.request.query_params.get('woman',None)
        name= self.request.query_params.get('name',None)
        #
        return Product.objects.filter_product( 
            man=man,
            woman=woman,
            name=name
        )

