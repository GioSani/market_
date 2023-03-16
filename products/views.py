from django.shortcuts import render, redirect


# Create your views here.
from django.http import HttpResponse

MY_ITEMS = [
    {'id': 1, 'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'id': 2,'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'id': 3,'name': 'wine', 'price': 10.0, 'quantity': 5},
]
from .models import Product,Order,OrderItem
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
            return redirect('products:product-list')
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


from .cart import Cart


def shoppingView(request):

    products = Product.objects.all()

    #del request.session['cart']
    cart = Cart(request)


    template_name = 'shopping.html'
    context = {
        'object_list':products,
        'cart':cart
    }
    return render(request,template_name,context)

def addToCard(request,id):

    product = Product.objects.get(id=id)
    quantity = int(request.GET.get('quantity'))
    cart =Cart(request)
    cart.add(product,quantity)
    cart.save()
    print(cart.cart)


    return redirect('products:shopping')

def deleteItemView(request,id):
    print('delete view--',id)
    cart = Cart(request)
    cart.delete(id)
    cart.save()
    return redirect('products:shopping')


@login_required
def checkoutView(request):
    template_name = 'checkout.html'
    cart = Cart(request)
    for c in cart:
        print(c)
    context = {
        'cart':cart
    }
    return render(request,template_name,context)

def makeOrderView(request):
    cart = Cart(request)
    if request.POST:
        order = Order(user=request.user)
        order.save()
        for item in cart:
            print('items---',item)
            orderItem = OrderItem(
                order=order,
                product_name=item.get('name'),
                quantity=item.get('quantity'),
                price=item.get('price')
            )
            orderItem.save()
        cart.clear()
        return HttpResponse('your order is set')
    return HttpResponse('not saved')

def myOrdersView(request):

    orders = Order.objects.filter(user=request.user)

    for order in orders:
        print('orderitem--',order.total_amount())

    template_name = 'my-orders.html'
    context = {
        'object_list': orders
    }
    return render(request,template_name,context)







