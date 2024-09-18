from django import forms 

from . import models as mdl 

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = mdl.ProductType
        fields = ['type_name',]
        widgets = {
            'type_name': forms.TextInput({
                'class':"form-control",
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
                'class':"form-control",
                'placeholder': 'Product Category...',
            }),

            'product_name': forms.TextInput({
                'class':"form-control",
                'placeholder': 'Product Name...',
                'autofocus':True,
            }),

            'price': forms.TextInput({
                'class':"form-control",
                'placeholder': 'Product price...',
            }),

            'image': forms.ClearableFileInput({
                "class":"form-control",
            }),

            'quantity': forms.NumberInput({
                "class":"form-control",
                'placeholder': 'Number of Products...',
            }),

            'description': forms.Textarea({
                'class':"form-control",
                'placeholder': 'Product Description...',
                'rows':3
            }),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = mdl.Order
        fields = ['id','quantity','customer']
        widgets = {
            'id': forms.HiddenInput({
                'class':"form-control",
            }),

            'quantity': forms.TextInput({
                'class':"form-control",
                'placeholder': 'Number Ordering ...',
                'required':True, 'autofocus':True
            }),

            'customer': forms.TextInput({
                'class':"form-control",
                'placeholder': 'Your Full Name...'
            }),
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = mdl.Order
        fields = ['status']
        widgets = {
            'status': forms.Select({
                'class':"form-control",
            }),
        }