from django.urls import path
from .views import productslistView, productView,eddProductView,editProductView,\
    deleteProductView,shoppingView,addToCard,deleteItemView,checkoutView,makeOrderView,myOrdersView
from . import views
app_name = 'products'
urlpatterns = [
    path('product-list',productslistView, name="product-list"),
    path('add-product',eddProductView,name="add-product"),
    path('edit-product/<int:id>',editProductView,name='edit-product'),
    path('delete-product/<int:id>',deleteProductView,name='delete-product'),
    path('product/<int:id>/',productView, name="product"),
    path('shopping/',shoppingView,name='shopping'),
    path('addToCard/<int:id>',addToCard,name='addToCard'),
    path('delete/<int:id>',deleteItemView,name='delete'),
    path('checkout/',checkoutView,name='checkout'),
    path('make-order',makeOrderView,name='make_order'),
    path('my-orders',myOrdersView,name='my_orders')


]
