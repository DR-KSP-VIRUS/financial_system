import json
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.validators import ValidationError
from django.db.models import Q
from django.db import connection
from django.contrib import messages


from . import models as mdl
from . import forms as fms
from accounts import forms as ac_fms

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    products = mdl.Product.objects.order_by('-updated').all()
    login_form = ac_fms.LoginForm()
    signup_form = ac_fms.SignupForm()
    context={
        "products":products,
        'form':login_form,
        'signupform':signup_form
    }
    return render(request, 'stores/index.html', context)

# ==================== search product in the shop ==================
def search_product(request):
    """ user enters the name of the product to search"""

    item_property = request.POST['search']
    #search here
    products = mdl.Product.objects.filter(
                                        Q(product_name__icontains=item_property)|
                                        Q(price__icontains=item_property)|
                                        Q(product_type__type_name__icontains=item_property)
                                    ).order_by("-expire_date").all()
    context = {
        "products":products,
        "item":item_property,
        }
    return render(request,"Seller/search_results.html",context)

# ====================== add product to database =====================
def add_product(request:HttpRequest) -> HttpResponse:
    """ add product type and the product to stock"""
    if request.method == "POST":
        # user has restock the shop
        form = fms.ProductForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            # valid data has been provided
            return redirect("stores:products")
    
def product_list(request:HttpRequest) -> HttpResponse:
    form = fms.ProductForm()
    products = mdl.Product.objects.all()
    context = {
        "form":form,
        "products":products
    }
    
    return render(request,"stores/products.html",context)


# ================== store product buy category ================
def add_category(request):
    """add catergoty of products sell by shop"""
    if request.method == "POST":
        # post the data
        form = fms.ProductTypeForm(data=request.POST)
        # validate the data
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.save()
            # go add add the products
            return redirect("stores:categories")

    
def category_list(request: HttpRequest) -> HttpResponse:
    # render empty form
    form = fms.ProductTypeForm()
    product_categories = mdl.ProductType.objects.all()
    context = {
        "form":form,
        "product_categories":product_categories,
    }
    return render(request,"stores/product_types.html",context)

def product_details(request,id):
    """ show the detailed description of the product"""
    product = get_object_or_404(mdl.Product,pk=id)
    context={
        "product":product,
    }
    return render(request,'stores/product.html',context)

def delete_product(request,pk):
    """delete the product from database"""
    product = get_object_or_404(mdl.Product,pk=pk)
    product.delete()
    return redirect("stores:products")

def delete_product_category(request,pk):
    """delete the product from database"""
    product = get_object_or_404(mdl.ProductType,pk=pk)
    product.delete()
    return redirect("stores:products")

def sales_list(request:HttpRequest) -> HttpResponse:
    orders = mdl.Order.objects.order_by('-updated').all()
    context = {
        'sales':orders
    }
    return render(request, 'stores/sales.html',context)

def place_orders(request:HttpRequest, *args, **kwargs) -> JsonResponse:
    orders = json.loads(request.body)
    if request.user.is_authenticated:
        for order in orders:
            product = get_object_or_404(mdl.Product, pk=order['id'])
            if product.quantity >= int(order['quantity']):
                product.quantity -= order['quantity']
                new_order = mdl.Order.objects.create(product=product,quantity=order['quantity'])
            else:
                return JsonResponse({"message":f"{product.product_name} has     quantity less that ordered quantity"})
            new_order.customer = request.user
            new_order.save()
            product.save()
        return JsonResponse({"message":"Order List Placement Successful."})
    return JsonResponse({'message':"Login to place your orders"})

def customer_orders(request:HttpRequest, *args, **kwargs) -> HttpResponse:
    context = {
    }
    return render(request, 'stores/my_orders.html', context)

def customer_json_orders(request:HttpRequest, *args, **kwargs) -> HttpResponse:
    orders = mdl.Order.objects.select_related('product').filter(customer=request.user).order_by('-created').all().values('product__product_name',                                                     'product__price',
      'quantity', 
      'created'
    )
    return JsonResponse({'orders':list(orders)})