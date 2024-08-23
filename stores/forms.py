from django import forms 

from . import models as mdl 

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = mdl.ProductType
        fields = ['type_name',]
        widgets = {
            'type_name': forms.TextInput({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
                'placeholder': 'Product Category...',
                'required':True, 'autofocus':True
            }),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = mdl.Product
        fields = ['product_type','product_name','price','image','quantity','description']
        widgets = {
            'product_type': forms.Select({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
                'placeholder': 'Product Category...',
            }),

            'product_name': forms.TextInput({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
                'placeholder': 'Product Name...',
                'autofocus':True,
            }),

            'price': forms.TextInput({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
                'placeholder': 'Product price...',
            }),

            'image': forms.ClearableFileInput({
                'class':"min-w-full border rounded px-2 py-0 border-orange-300 focus-within:outline-orange-500",
            }),

            'quantity': forms.NumberInput({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
                'placeholder': 'Number of Products...',
            }),

            'description': forms.Textarea({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
                'placeholder': 'Product Description...',
                'rows':3
            }),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = mdl.Order
        fields = ['id','quantity','client_name','phone']
        widgets = {
            'id': forms.HiddenInput({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
            }),

            'quantity': forms.TextInput({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
                'placeholder': 'Number Ordering ...',
                'required':True, 'autofocus':True
            }),

            'client_name': forms.TextInput({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
                'placeholder': 'Your Full Name...'
            }),

            'phone': forms.TextInput({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
                'placeholder': 'Your Phone Number'
            }),
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = mdl.Order
        fields = ['status']
        widgets = {
            'status': forms.Select({
                'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
            }),
        }