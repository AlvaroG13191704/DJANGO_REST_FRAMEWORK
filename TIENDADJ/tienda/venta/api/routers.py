from rest_framework.routers import DefaultRouter
#
from . import viewsets
#
router = DefaultRouter()

router.register(r'sales',viewsets.SaleViewSet,basename='sales')
urlpatterns = router.urls