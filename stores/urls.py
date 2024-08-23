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
    
    # home
    # path('',main_views.index_page,name="home"),
    # # add to stock

    # path('add-to-stock/',main_views.add_to_stock,name="add-to-stock"),
    # path('add/category/',main_views.add_category,name='category'),
    # path('expenses',main_views.set_expenses,name="expenses"),
    # # profile

    # path('profile/',main_views.profile,name="profile"),
    # path('product/editor/<int:product_id>/edit',main_views.edit_product_info,name="edit_product"),
    # path('delete/item-number/<int:item_id>-from/database',main_views.delete_product,name="delete-item"),
    
    # # orders
    # path('my/order/',main_views.myOrders,name="my-orders"),
    # path('clear/my/orders',main_views.clear_orders,name="clear-orders"),
    # path('add/<int:product_id>to/cart',main_views.add_to_cart,name="add-to-cart"),
    
    # # search
    # path('searched/results/',main_views.search_product,name='search-results'),
    # path('show/<int:productId>/detailed-description/',main_views.show_product_description,name='show-description'),
]
