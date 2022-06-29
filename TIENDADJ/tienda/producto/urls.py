#django
from django.urls import path
#views
from . import views

urlpatterns = [
    path(
        'api/product/per-user/',
        views.ListProductUser.as_view(),
        name='product-by-user'
    ),
    path(
        'api/product/per-stok/',
        views.ListProductStok.as_view(),
        name='product-by-stok'
    ),
    path(
        'api/product/per-gender/<gender>/',
        views.ListProductGender.as_view(),
        name='product-by-gender'
    ),
    path(
        'api/product/filter/',
        views.FilterProducts.as_view(),
        name='product-filter'
    )
]