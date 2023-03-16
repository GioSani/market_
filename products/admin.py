from django.contrib import admin

# Register your models here.
from .models import Product,Order,OrderItem
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','quantity')

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id','product_id','customer_id')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','date_created','date_updated')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','order','price','quantity')