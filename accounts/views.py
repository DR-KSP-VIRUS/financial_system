from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from . import models as mdl
from . import forms as fms
from stores import models as smdl

# Create your views here.

def user_login_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = fms.LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user=user)
                if user.is_customer:
                    return redirect('stores:my-orders')
                return redirect('accounts:dashboard')
            return redirect('stores:home')
        return redirect('stores:home')
    return redirect('stores:home')

def signup(request:HttpRequest, *args, **kwargs) -> HttpResponse:
    if request.method == 'POST':
        form = fms.SignupForm(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('stores:home')
    return redirect('stores:home')

@login_required  
def user_dashboard(request:HttpRequest) -> HttpResponse:
    products = smdl.Product.objects.all()
    categories = smdl.ProductType.objects.all()
    orders = smdl.Order.objects.all()
    today_orders = smdl.Order.today_orders()
    print(today_orders)
    context = {
        "products":products,
        "categories":categories,
        "orders":orders
    }
    return render(request, 'accounts/dashboard.html',context)

@login_required
def user_logout(request:HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('stores:home')