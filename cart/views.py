from django.shortcuts import render
from django.views import View

from .cart import Cart


class AddToCart(View):
    def get(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        cart.add(product_id)
        return render(request, 'cart/menu_cart.html')
