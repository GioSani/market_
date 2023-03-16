from .models import Product

CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        print('iter daiqoa--------------------------------------------')
        for product in products:
            cart[str(product.id)]['product'] = product

        return iter(cart.values())

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price': str(product.price),'name':product.name}
        self.cart[product_id]['quantity'] += quantity

    def delete(self,id):
        self.cart.pop(str(id))
        print('delete class--',id,self.cart)

    def clear(self):
        del self.session[CART_SESSION_ID]

    def save(self):
        self.session.modified = True