from datetime import datetime
from django.db import models
from django.db.models import Count, Sum
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class ProductType(models.Model):
    """ model of products at shop"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product_type')
    type_name = models.CharField("Product Type:",max_length=50,null=False)


    class Meta:
        verbose_name_plural = "Product Type"

    def __str__(self):
        """ string representation of the product type"""
        return self.type_name



class Product(models.Model):
    """ individual products in the shop """
    product_type = models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='product_types')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_products')
    product_name = models.CharField("Product Name:",max_length=25)
    price = models.DecimalField("Product Price:",max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    quantity = models.IntegerField("No. of Products:",default=0)
    description = models.TextField('Description',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = ("Products")
    
    def __str__(self):
        """ string representation of the product name"""
        return self.product_name


class Order(models.Model):
    """products soled in a day"""
    STATUS = (
        ('','...'),('p', 'Pending'),
        ('d', 'Delivered'),('f', 'Failed'),
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_sales')
    quantity = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='customer_orders')
    status = models.CharField(max_length=5,choices=STATUS, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name
    

    @classmethod
    def today_orders(cls):
        return [
            order for order in cls.objects.values('product__product_name', 'customer__full_name', 'created','quantity', 'product__price').annotate(order_quantity=Count('product__product_name'), total=Sum('product__price'))
            if order['created'].date() == datetime.today().date()
    ]
    
    @classmethod
    def a_week_orders(cls):
        # datetime.weekday
        return [
            order  for order in cls.objects.filter(created=datetime(datetime.now().year, datetime.now().month-1, 1)).values('product__product_name','created','quantity', 'product__price').annotate(order_quantity=Count('product__product_name'), total=Sum('product__price'))
        ]

