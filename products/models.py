from django.db import models
from customers.models import Customer
# Create your models here.
from registration.models import User
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()




    def __str__(self):
        return self.name

# class Order(models.Model):
#     product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
#     customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def total_amount(self):
        total_amount = 0
        items = OrderItem.objects.filter(order = self.id).aggregate(models.Sum('price',field='price*quantity'))
        # for item in items:
        #     total_amount += item.quantity*item.price
        return items.get('price__sum')

    def quantity(self):
        quantity = OrderItem.objects.filter(order=self.id).aggregate(models.Sum('quantity'))
        return quantity.get('quantity__sum')

    def items(self):
        items = OrderItem.objects.filter(order=self.id)
        return items


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    #product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2)


