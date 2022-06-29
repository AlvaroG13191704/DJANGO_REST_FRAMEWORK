from django.db import models

#
class SaleDetailManager(models.Manager):
    #deffs
    def products_per_sale(self,sail_id):
        return self.filter(
            sale__id = sail_id,
        ).order_by('count','product__name')