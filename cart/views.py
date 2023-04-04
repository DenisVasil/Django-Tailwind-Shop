from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .cart import Cart
from product.models import Product


class AddToCart(View):
    def get(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        cart.add(product_id)
        return render(request, 'cart/menu_cart.html')


class Cart(TemplateView):
    template_name = 'cart/cart.html'


class Checkout(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    template_name = 'cart/checkout.html'


class UpdateCart(View):
    def update_cart(request, product_id, action):
        cart = Cart(request)

        if action == 'increment':
            cart.add(product_id, 1, True)
        else:
            cart.add(product_id, -1, True)

        product = Product.objects.get(pk=product_id)
        quantity = cart.get_item(product_id)['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'get_thumbnail': product.get_thumbnail(),
                'price': product.price,
            },
            'total_price': (quantity * product.price) / 100,
            'quantity': quantity,
        }

        response = render(
            request, 'cart/partials/cart_item.html', {'item': item})
        response['HX-Trigger'] = 'update-menu-cart'

        return response


class Hx_menu_cart(TemplateView):
    template_name = 'cart/menu_cart.html'


class Hx_cart_total(TemplateView):
    template_name = 'cart/partials/cart_total.html'
