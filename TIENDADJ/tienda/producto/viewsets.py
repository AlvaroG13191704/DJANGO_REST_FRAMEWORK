from rest_framework import viewsets

#model
from .models import Colors,Product
#
from .serializers import ColorsSerializer,ProductSerializer, ProductPagination, ProductSerializer2

#viewsert

class ColorViewSet(viewsets.ModelViewSet):
    #as always
    serializer_class = ColorsSerializer
    #parameters
    queryset = Colors.objects.all()

#products
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer2
    queryset = Product.objects.all()
    #pagination
    pagination_class=ProductPagination

    #special deff
    def perform_create(self, serializer):
        serializer.save(
            video='https://www.youtube.com/watch?v=C7-uoN8pcmE&ab_channel=Neunapp'
        )

