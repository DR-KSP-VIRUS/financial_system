from django.urls import path

from . import views as v

app_name = 'stores'

urlpatterns = [
    path('',v.index, name='home'),
    path('add-category',v.add_category, name='add-category'),
    path('categories',v.category_list, name='categories'),
    path('add-product',v.add_product, name='add-product'),
    path('products',v.product_list, name='products'),
    path('sales',v.sales_list, name='sales'),
    path('place-orders',v.place_orders, name='place-orders'),
    path('my-orders', v.customer_orders, name='my-orders'),
    path('my-orders-json', v.customer_json_orders, name='my-orders-ajax'),
]
