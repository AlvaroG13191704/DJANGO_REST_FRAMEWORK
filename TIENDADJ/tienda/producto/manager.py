from django.db import models

class ProductManager(models.Manager):

    def products_per_user(self,user):
        return self.filter(
            user_created = user,
        )

    def products_w_stok(self):
        return self.filter(
            stok__gt=0,
        ).order_by('-num_sales')
    
    def products_b_gender(self,gender):
        #list by gender
        if gender == 'm':
            w = True
            m = False
        elif gender == 'w':
            m = True
            w = False
        elif gender == 'o':
            m = True
            w = True
        #filter
        return self.filter(
            woman = w,
            man = m
        ).order_by('created')
    
    def filter_product(self,**filters):
        return self.filter(
            man = filters['man'],
            woman = filters['woman'],
            name__icontains = filters['name']
        )
