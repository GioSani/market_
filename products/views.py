from django.shortcuts import render, redirect


# Create your views here.
from django.http import HttpResponse

MY_ITEMS = [
    {'id': 1, 'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'id': 2,'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'id': 3,'name': 'wine', 'price': 10.0, 'quantity': 5},
]
from .models import Product,Order
from customers.models import Customer
from django.contrib.auth.decorators import login_required



@login_required
def productslistView(request):
    print(request.user)


    products = Product.objects.all()
    context = {
        'object_list':products,
    }
    template_name = "productslist.html"
    return render(request, template_name, context)


@login_required
def productView(request, id):
    product = Product.objects.get(id=id)
    template_name = "product.html"
    context = {
        'object':product
    }
    return render(request, template_name, context)

from .forms import ProductForm

def eddProductView(request):
    template_name = "addProduct.html"
    form = ProductForm()

    if request.POST:
        form = ProductForm(request.POST)
        print('post test--------')

        if form.is_valid():
            form.save()
            return redirect('product-list')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request,template_name,context)

def editProductView(request,id):

    template_name = 'editProduct.html'
    product = Product.objects.get(id=id)

    form = ProductForm(instance=product)
    if request.POST:
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()

            return redirect('product-list')

    context = {
        'form': form,
        'product_id': product.id,
    }
    return render(request,template_name,context)

def deleteProductView(request,id):
    print('delete datrigerda')
    product = Product.objects.get(id=id)
    if request.POST:
        product.delete()
    return redirect('product-list')

