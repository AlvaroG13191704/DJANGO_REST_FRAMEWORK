#
from django.urls import path
#viers
from . import views

urlpatterns = [
    path(
        'api/sale/report/',
        views.ListReportSales.as_view(),
        name='report-sale'
    ),
    path(
        'api/create/sail/',
        views.RegisterSail.as_view(),
        name='register-sale'
    ),
    path(
        'api/create/sail-2/',
        views.RegisterSail2.as_view(),
        name='register-sale'
    ),
]